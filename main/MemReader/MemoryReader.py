import pymem


class MemoryReader:
    def __init__(self):
        self.process_name = "cs2.exe"

    def read_game_memory(self):
        try:
            pm = pymem.Pymem(self.process_name)
            client = pymem.process.module_from_name(
                pm.process_handle, "client.dll"
            ).lpBaseOfDll

            player_base = pm.read_int(client + 0x10F4F4)
            if not player_base or player_base <= 0:
                raise ValueError(
                    f"{player_base}")

            x_coord = pm.read_float(player_base + 0x134)
            y_coord = pm.read_float(player_base + 0x138)
            z_coord = pm.read_float(player_base + 0x13C)

            return f"Coordinates: X={x_coord}, Y={y_coord}, Z={z_coord}"
        except pymem.exception.MemoryReadError as e:
            raise RuntimeError(
                f"{e}.")
        except ValueError as ve:
            raise RuntimeError(f"Validation error: {ve}")
        except Exception as e:
            raise RuntimeError(
                f"{e}")


if __name__ == "__main__":
    import time

    memory_reader = MemoryReader()
    while True:
        try:
            result = memory_reader.read_game_memory()
            print(result)
        except RuntimeError as e:
            print(f"[ERROR] {e}")

        time.sleep(0.5)
