class WavFile:
    hour_in_sec = 3600
    kb_to_gb = 1024**3
    kb_to_mb = 1024
    bits = 8
    kilobits = 0

    def __init__(self, bits_psec, sample_psec, num_ch, duration):
        self.bits_psec = bits_psec
        self.sample_psec = sample_psec
        self.num_ch = num_ch
        self.duration = duration

    def min_sec(self):
        return self.duration * 60

    def check_size(self, size):
        if size >= self.hour_in_sec:
            return round(size, 2)

        elif size < self.hour_in_sec:
            return round(size, 2)

    def get_bitrate(self, channels):
        bitrate = self.bits_psec * self.sample_psec * channels
        kbps = bitrate / 1000
        self.kilobits += kbps
        return bitrate

    def get_size_gb(self):
        file_size = (
            self.get_bitrate(self.num_ch) * self.min_sec()) / self.bits / self.kb_to_gb
        )
        return self.check_size(file_size)

new_file = WavFile(24, 48000, 4, 60)
print(new_file.get_size_gb())
print(new_file.kilobits)
