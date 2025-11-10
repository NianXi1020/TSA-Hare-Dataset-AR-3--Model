import math
from typing import List, Tuple

# Basic grayscale drawing utilities

def create_canvas(width: int, height: int, value: int = 255) -> List[List[int]]:
    return [[value for _ in range(width)] for _ in range(height)]


def clamp(value: int, low: int, high: int) -> int:
    return max(low, min(high, value))


def draw_line(canvas: List[List[int]], x0: float, y0: float, x1: float, y1: float, color: int) -> None:
    width = len(canvas[0])
    height = len(canvas)
    x0 = int(round(x0))
    y0 = int(round(y0))
    x1 = int(round(x1))
    y1 = int(round(y1))
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    while True:
        if 0 <= x0 < width and 0 <= y0 < height:
            canvas[y0][x0] = clamp(color, 0, 255)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


def fill_rect(canvas: List[List[int]], x0: float, y0: float, x1: float, y1: float, color: int) -> None:
    width = len(canvas[0])
    height = len(canvas)
    left = int(round(min(x0, x1)))
    right = int(round(max(x0, x1)))
    top = int(round(min(y0, y1)))
    bottom = int(round(max(y0, y1)))
    left = max(0, left)
    right = min(width - 1, right)
    top = max(0, top)
    bottom = min(height - 1, bottom)
    for y in range(top, bottom + 1):
        row = canvas[y]
        for x in range(left, right + 1):
            row[x] = clamp(color, 0, 255)


def draw_point(canvas: List[List[int]], x: float, y: float, radius: int, color: int) -> None:
    width = len(canvas[0])
    height = len(canvas)
    cx = int(round(x))
    cy = int(round(y))
    for dy in range(-radius, radius + 1):
        for dx in range(-radius, radius + 1):
            px = cx + dx
            py = cy + dy
            if 0 <= px < width and 0 <= py < height:
                if dx * dx + dy * dy <= radius * radius:
                    canvas[py][px] = clamp(color, 0, 255)

FONT_5X7 = {
    ' ': [
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
    ],
    'A': [
        "01110",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001",
    ],
    'C': [
        "01110",
        "10001",
        "10000",
        "10000",
        "10000",
        "10001",
        "01110",
    ],
    'D': [
        "11110",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "11110",
    ],
    'E': [
        "11111",
        "10000",
        "10000",
        "11110",
        "10000",
        "10000",
        "11111",
    ],
    'F': [
        "11111",
        "10000",
        "10000",
        "11110",
        "10000",
        "10000",
        "10000",
    ],
    'G': [
        "01110",
        "10001",
        "10000",
        "10111",
        "10001",
        "10001",
        "01110",
    ],
    'H': [
        "10001",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001",
    ],
    'I': [
        "11111",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
        "11111",
    ],
    'L': [
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "11111",
    ],
    'M': [
        "10001",
        "11011",
        "10101",
        "10101",
        "10001",
        "10001",
        "10001",
    ],
    'N': [
        "10001",
        "11001",
        "10101",
        "10011",
        "10001",
        "10001",
        "10001",
    ],
    'O': [
        "01110",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "01110",
    ],
    'P': [
        "11110",
        "10001",
        "10001",
        "11110",
        "10000",
        "10000",
        "10000",
    ],
    'Q': [
        "01110",
        "10001",
        "10001",
        "10001",
        "10101",
        "10010",
        "01101",
    ],
    'R': [
        "11110",
        "10001",
        "10001",
        "11110",
        "10100",
        "10010",
        "10001",
    ],
    'S': [
        "01111",
        "10000",
        "10000",
        "01110",
        "00001",
        "00001",
        "11110",
    ],
    'T': [
        "11111",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
    ],
    'U': [
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "01110",
    ],
    'V': [
        "10001",
        "10001",
        "10001",
        "10001",
        "01010",
        "01010",
        "00100",
    ],
    'Y': [
        "10001",
        "10001",
        "01010",
        "00100",
        "00100",
        "00100",
        "00100",
    ],
    'G': [
        "01110",
        "10001",
        "10000",
        "10111",
        "10001",
        "10001",
        "01110",
    ],
    '0': [
        "01110",
        "10001",
        "10011",
        "10101",
        "11001",
        "10001",
        "01110",
    ],
    '1': [
        "00100",
        "01100",
        "00100",
        "00100",
        "00100",
        "00100",
        "01110",
    ],
    '2': [
        "01110",
        "10001",
        "00001",
        "00010",
        "00100",
        "01000",
        "11111",
    ],
    '3': [
        "11110",
        "00001",
        "00001",
        "01110",
        "00001",
        "00001",
        "11110",
    ],
    '4': [
        "00010",
        "00110",
        "01010",
        "10010",
        "11111",
        "00010",
        "00010",
    ],
    '5': [
        "11111",
        "10000",
        "11110",
        "00001",
        "00001",
        "10001",
        "01110",
    ],
    '6': [
        "00110",
        "01000",
        "10000",
        "11110",
        "10001",
        "10001",
        "01110",
    ],
    '7': [
        "11111",
        "00001",
        "00010",
        "00100",
        "01000",
        "01000",
        "01000",
    ],
    '8': [
        "01110",
        "10001",
        "10001",
        "01110",
        "10001",
        "10001",
        "01110",
    ],
    '9': [
        "01110",
        "10001",
        "10001",
        "01111",
        "00001",
        "00010",
        "01100",
    ],
    '-': [
        "00000",
        "00000",
        "00000",
        "11111",
        "00000",
        "00000",
        "00000",
    ],
    '.': [
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
        "01100",
        "01100",
    ],
    '(': [
        "00110",
        "01000",
        "10000",
        "10000",
        "10000",
        "01000",
        "00110",
    ],
    ')': [
        "01100",
        "00010",
        "00001",
        "00001",
        "00001",
        "00010",
        "01100",
    ],
}

# Ensure missing characters fall back to space

def draw_char(canvas: List[List[int]], x: int, y: int, ch: str, color: int) -> None:
    glyph = FONT_5X7.get(ch.upper(), FONT_5X7[' '])
    height = len(canvas)
    width = len(canvas[0])
    for row_idx, row_bits in enumerate(glyph):
        for col_idx, bit in enumerate(row_bits):
            if bit == '1':
                px = x + col_idx
                py = y + row_idx
                if 0 <= px < width and 0 <= py < height:
                    canvas[py][px] = clamp(color, 0, 255)


def draw_text(canvas: List[List[int]], x: int, y: int, text: str, color: int, spacing: int = 1) -> None:
    cursor_x = x
    for ch in text:
        draw_char(canvas, cursor_x, y, ch, color)
        cursor_x += 5 + spacing

# JPEG encoding utilities

ZIGZAG = [
    0, 1, 5, 6,14,15,27,28,
    2, 4, 7,13,16,26,29,42,
    3, 8,12,17,25,30,41,43,
    9,11,18,24,31,40,44,53,
   10,19,23,32,39,45,52,54,
   20,22,33,38,46,51,55,60,
   21,34,37,47,50,56,59,61,
   35,36,48,49,57,58,62,63,
]

LUMA_Q = [
    16, 11, 10, 16, 24, 40, 51, 61,
    12, 12, 14, 19, 26, 58, 60, 55,
    14, 13, 16, 24, 40, 57, 69, 56,
    14, 17, 22, 29, 51, 87, 80, 62,
    18, 22, 37, 56, 68,109,103, 77,
    24, 35, 55, 64, 81,104,113, 92,
    49, 64, 78, 87,103,121,120,101,
    72, 92, 95, 98,112,100,103, 99,
]

LUMA_DC_BITS = [0, 1, 5, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
LUMA_DC_VALS = list(range(12))
LUMA_AC_BITS = [0, 2, 1, 3, 3, 2, 4, 3, 5, 5, 4, 4, 0, 0, 1, 0x7D]
LUMA_AC_VALS = [
    0x01,0x02,0x03,0x00,0x04,0x11,0x05,0x12,0x21,0x31,0x41,0x06,0x13,0x51,0x61,
    0x07,0x22,0x71,0x14,0x32,0x81,0x91,0xA1,0x08,0x23,0x42,0xB1,0xC1,0x15,0x52,
    0xD1,0xF0,0x24,0x33,0x62,0x72,0x82,0x09,0x0A,0x16,0x17,0x18,0x19,0x1A,0x25,
    0x26,0x27,0x28,0x29,0x2A,0x34,0x35,0x36,0x37,0x38,0x39,0x3A,0x43,0x44,0x45,
    0x46,0x47,0x48,0x49,0x4A,0x53,0x54,0x55,0x56,0x57,0x58,0x59,0x5A,0x63,0x64,
    0x65,0x66,0x67,0x68,0x69,0x6A,0x73,0x74,0x75,0x76,0x77,0x78,0x79,0x7A,0x83,
    0x84,0x85,0x86,0x87,0x88,0x89,0x8A,0x92,0x93,0x94,0x95,0x96,0x97,0x98,0x99,
    0x9A,0xA2,0xA3,0xA4,0xA5,0xA6,0xA7,0xA8,0xA9,0xAA,0xB2,0xB3,0xB4,0xB5,0xB6,
    0xB7,0xB8,0xB9,0xBA,0xC2,0xC3,0xC4,0xC5,0xC6,0xC7,0xC8,0xC9,0xCA,0xD2,0xD3,
    0xD4,0xD5,0xD6,0xD7,0xD8,0xD9,0xDA,0xE1,0xE2,0xE3,0xE4,0xE5,0xE6,0xE7,0xE8,
    0xE9,0xEA,0xF1,0xF2,0xF3,0xF4,0xF5,0xF6,0xF7,0xF8,0xF9,0xFA,
]

COS_TABLE = [[math.cos((2 * x + 1) * u * math.pi / 16.0) for x in range(8)] for u in range(8)]
C_FACTORS = [1 / math.sqrt(2.0)] + [1.0] * 7


def pad_pixels(pixels: List[List[int]]) -> Tuple[List[List[int]], int, int]:
    height = len(pixels)
    width = len(pixels[0])
    padded_width = (width + 7) // 8 * 8
    padded_height = (height + 7) // 8 * 8
    padded = [[0] * padded_width for _ in range(padded_height)]
    for y in range(padded_height):
        src_y = min(y, height - 1)
        src_row = pixels[src_y]
        padded_row = padded[y]
        for x in range(padded_width):
            src_x = min(x, width - 1)
            padded_row[x] = src_row[src_x]
    return padded, padded_width, padded_height


def dct_block(block: List[List[int]]) -> List[List[float]]:
    transformed = [[0.0] * 8 for _ in range(8)]
    for v in range(8):
        for u in range(8):
            acc = 0.0
            for y in range(8):
                for x in range(8):
                    acc += block[y][x] * COS_TABLE[u][x] * COS_TABLE[v][y]
            transformed[v][u] = 0.25 * C_FACTORS[u] * C_FACTORS[v] * acc
    return transformed


def quantize_block(transformed: List[List[float]]) -> List[int]:
    coeffs = [0] * 64
    for idx, pos in enumerate(ZIGZAG):
        row = pos // 8
        col = pos % 8
        value = transformed[row][col] / LUMA_Q[row * 8 + col]
        coeffs[idx] = int(round(value))
    return coeffs


def build_huffman(bits: List[int], vals: List[int]):
    huff = {}
    code = 0
    k = 0
    for bit_len in range(1, 17):
        count = bits[bit_len - 1]
        for _ in range(count):
            huff[vals[k]] = (code, bit_len)
            code += 1
            k += 1
        code <<= 1
    return huff

DC_HUFF = build_huffman(LUMA_DC_BITS, LUMA_DC_VALS)
AC_HUFF = build_huffman(LUMA_AC_BITS, LUMA_AC_VALS)


def magnitude_category(value: int) -> int:
    if value == 0:
        return 0
    abs_val = abs(value)
    cat = 0
    while abs_val:
        abs_val >>= 1
        cat += 1
    return cat


def encode_magnitude(value: int, size: int) -> int:
    if size == 0:
        return 0
    if value >= 0:
        return value
    return (1 << size) + value - 1


class BitWriter:
    def __init__(self) -> None:
        self.data = bytearray()
        self.buffer = 0
        self.bit_count = 0

    def write(self, code: int, length: int) -> None:
        for shift in range(length - 1, -1, -1):
            bit = (code >> shift) & 1
            self.buffer = (self.buffer << 1) | bit
            self.bit_count += 1
            if self.bit_count == 8:
                byte = self.buffer & 0xFF
                self.data.append(byte)
                if byte == 0xFF:
                    self.data.append(0x00)
                self.buffer = 0
                self.bit_count = 0

    def flush(self) -> None:
        if self.bit_count > 0:
            self.buffer <<= (8 - self.bit_count)
            byte = self.buffer & 0xFF
            self.data.append(byte)
            if byte == 0xFF:
                self.data.append(0x00)
            self.buffer = 0
            self.bit_count = 0


def encode_blocks(pixels: List[List[int]]) -> bytearray:
    padded, padded_width, padded_height = pad_pixels(pixels)
    writer = BitWriter()
    prev_dc = 0
    for by in range(0, padded_height, 8):
        for bx in range(0, padded_width, 8):
            block = [[padded[by + y][bx + x] - 128 for x in range(8)] for y in range(8)]
            transformed = dct_block(block)
            coeffs = quantize_block(transformed)
            dc = coeffs[0]
            diff = dc - prev_dc
            prev_dc = dc
            cat = magnitude_category(diff)
            code, length = DC_HUFF[cat]
            writer.write(code, length)
            if cat > 0:
                writer.write(encode_magnitude(diff, cat), cat)
            run = 0
            for coeff in coeffs[1:]:
                if coeff == 0:
                    run += 1
                else:
                    while run > 15:
                        code, length = AC_HUFF[0xF0]
                        writer.write(code, length)
                        run -= 16
                    cat = magnitude_category(coeff)
                    symbol = (run << 4) | cat
                    code, length = AC_HUFF[symbol]
                    writer.write(code, length)
                    writer.write(encode_magnitude(coeff, cat), cat)
                    run = 0
            if run > 0:
                code, length = AC_HUFF[0x00]
                writer.write(code, length)
    writer.flush()
    return writer.data


def write_segment(output: bytearray, marker: int, payload: bytes) -> None:
    output.extend(b"\xFF" + bytes([marker]))
    length = len(payload) + 2
    output.extend(length.to_bytes(2, 'big'))
    output.extend(payload)


def save_grayscale_jpeg(filename: str, pixels: List[List[int]]) -> None:
    height = len(pixels)
    width = len(pixels[0])
    compressed = encode_blocks(pixels)

    output = bytearray()
    output.extend(b"\xFF\xD8")

    app0 = bytearray(b"JFIF\x00")
    app0.extend(b"\x01\x01")
    app0.extend(b"\x00")
    app0.extend(b"\x00\x48")
    app0.extend(b"\x00\x48")
    app0.extend(b"\x00\x00")
    write_segment(output, 0xE0, app0)

    dqt_payload = bytes([0x00] + LUMA_Q)
    write_segment(output, 0xDB, dqt_payload)

    sof = bytearray()
    sof.append(8)
    sof.extend(height.to_bytes(2, 'big'))
    sof.extend(width.to_bytes(2, 'big'))
    sof.append(1)
    sof.extend(b"\x01\x11\x00")
    write_segment(output, 0xC0, sof)

    def build_dht_payload(bits: List[int], vals: List[int], table_class: int, table_id: int) -> bytes:
        payload = bytearray()
        payload.append((table_class << 4) | table_id)
        payload.extend(bits)
        payload.extend(vals)
        return bytes(payload)

    dht = bytearray()
    dht.extend(build_dht_payload(LUMA_DC_BITS, LUMA_DC_VALS, 0, 0))
    dht.extend(build_dht_payload(LUMA_AC_BITS, LUMA_AC_VALS, 1, 0))
    write_segment(output, 0xC4, dht)

    sos = bytearray()
    sos.append(1)
    sos.extend(b"\x01\x00")
    sos.extend(b"\x00\x3F\x00")
    write_segment(output, 0xDA, sos)

    output.extend(compressed)
    output.extend(b"\xFF\xD9")

    with open(filename, 'wb') as f:
        f.write(output)
