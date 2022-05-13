from scipy.io import wavfile


def zero_crossing_extractor(audio, sr=44100, silence_thr=0):
    """
    Extracts the fundamental frequency given an input sound. Limitations: only works well with pure tones.
    :param audio: the input sound
    :param fs: the sampling frequency
    :param silence_thr: the threshold that we count as 0
    :return: the estimated fundamental frequency
    """
    num_samples = len(audio)
    num_crossing = 0  # number of crossings

    # compute number of crossings
    for i in range(num_samples - 1):
        if (audio[i] > silence_thr >= audio[i + 1]) or (
            audio[i] < silence_thr <= audio[i + 1]
        ):
            num_crossing += 1

    total_seconds = num_samples / sr
    num_cycles = num_crossing / 2
    frequency = num_cycles / total_seconds

    return frequency

"""
# INFORMAL TEST todo move to tests
sr, audio = wavfile.read("../sounds/sine-101.wav")

print(zero_crossing_extractor(audio))
"""