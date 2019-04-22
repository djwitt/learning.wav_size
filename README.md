# Wav File Size
*verison 1.0*
#### Calculating the estimated size of a WAV file

Example:
``` python
import WavFile

wav = WavFile(24, 48000, 4, 60)
wav_size = wav.get_size_gb()
wav_kbps = wav.kilobits

print(wav_size)    # 1.93   (in GB)
print(wav_kbps)    # 4608.0 (in kbps)

```

## Usage
`WavFile` requires *Bit Depth*, *Sampling Rate*, *Number of Channels*, and *File length in Minutes*

**get_size_gb()**
This gets the estimated file size in Gigabytes

**kilobits**
If you would like to see data rate of the estimated wave file
