import fefeditor2

from paragon.core.bin_streams import BinArchiveReader, BinArchiveWriter
from paragon.module.properties.i32_property import I32Property
from paragon.module.properties.property_container import PropertyContainer
from paragon.module.properties.string_property import StringProperty

TILE_TEMPLATE = None
_GRID_SIZE = 1048
_TILE_SIZE = 0x28
_HEADER_SIZE = 0x10


def load_tile_template():
    global TILE_TEMPLATE
    if not TILE_TEMPLATE:
        TILE_TEMPLATE = PropertyContainer.from_file("Modules/ServiceData/FE14Tile.json")


def get_tile_template():
    global TILE_TEMPLATE
    return TILE_TEMPLATE


class Terrain:
    def __init__(self):
        self.tiles = []
        self.grid = [[0 for _ in range(32)] for _ in range(32)]
        self.map_model = StringProperty("Map Model")
        self.map_size_x = I32Property("Map Size X")
        self.map_size_y = I32Property("Map Size Y")
        self.border_size_x = I32Property("Border Size X")
        self.border_size_y = I32Property("Border Size Y")
        self.trimmed_size_x = I32Property("Trimmed Size X")
        self.trimmed_size_y = I32Property("Trimmed Size Y")
        self._adapter = self._create_property_form_adapter()

    def read(self, archive):
        reader = BinArchiveReader(archive)
        tile_table_address = reader.read_internal_pointer()
        tile_count = reader.read_u32()
        self.map_model.read(reader)
        grid_address = reader.read_internal_pointer()

        self.tiles.clear()
        reader.seek(tile_table_address)
        for _ in range(0, tile_count):
            tile = self._read_tile(reader)
            self.tiles.append(tile)

        reader.seek(grid_address)
        self.map_size_x.read(reader)
        self.map_size_y.read(reader)
        self.border_size_x.read(reader)
        self.border_size_y.read(reader)
        self.trimmed_size_x.read(reader)
        self.trimmed_size_y.read(reader)
        for r in range(0, 32):
            for c in range(0, 32):
                self.grid[r][c] = reader.read_u8()

    def _create_property_form_adapter(self):
        adapter = {
            "Map Model": self.map_model,
            "Map Size X": self.map_size_x,
            "Map Size Y": self.map_size_y,
            "Border Size X": self.border_size_x,
            "Border Size Y": self.border_size_y,
            "Trimmed Size X": self.trimmed_size_x,
            "Trimmed Size Y": self.trimmed_size_y,
        }
        return adapter

    @staticmethod
    def _read_tile(reader):
        if not TILE_TEMPLATE:
            load_tile_template()
        tile = TILE_TEMPLATE.duplicate()
        for prop in tile.values():
            prop.read(reader)
        return tile

    def adapter(self):
        return self._adapter

    def to_bin(self):
        archive = fefeditor2.create_bin_archive()
        archive.allocate_at_end(self._calculate_binary_size())
        writer = BinArchiveWriter(archive)
        writer.write_pointer(_HEADER_SIZE)
        writer.write_u32(len(self.tiles))
        self.map_model.write(writer)
        writer.write_pointer(self._grid_address())
        for tile in self.tiles:
            for prop in tile.values():
                prop.write(writer)
        self.map_size_x.write(writer)
        self.map_size_y.write(writer)
        self.border_size_x.write(writer)
        self.border_size_y.write(writer)
        self.trimmed_size_x.write(writer)
        self.trimmed_size_y.write(writer)
        for row in self.grid:
            writer.write_bytes(row)
        return archive

    def _calculate_binary_size(self):
        return _HEADER_SIZE + len(self.tiles) * _TILE_SIZE + _GRID_SIZE

    def _grid_address(self):
        return _HEADER_SIZE + len(self.tiles) * _TILE_SIZE
