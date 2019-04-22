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

### Usage
`WavFile` requires *Bit Depth*, *Sampling Rate*, *Number of Channels*, and *File length in Minutes*

**get_size_gb()**
This gets the estimated file size in Gigabytes

**kilobits**
If you would like to see data rate of the estimated wave file


!!! note Notes for development
Bitrate is the number of bits per second
`bitrate = bitsPerSecond * samplePerSec * #channels`

File size is calculated by multiplying the bitrate by the duration (in seconds) and is then divide by 8 (from bits to bytes)
`fileSize = (bitsPerSample * samplePerSec * #CH * duration) / 8`
!!!
