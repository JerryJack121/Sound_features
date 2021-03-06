import os
import librosa
from wav_helper import Wav_helper as Wav
import matplotlib.pyplot as plt
from scipy import signal
import soundfile as sf

# 濾波器
def filter(sig, sr, fx, mode):
    wn = 2 * fx / sr
    b, a = signal.butter(8, wn, mode)  #配置濾波器 8 表示濾波器的階數
    sig2 = signal.filtfilt(b, a, sig)
    return sig2


audio_path = r'D:\dataset\鳥叫聲\晨間霧水滴落在葉子的聲音'
audio_name = '官田區2.wav'

# load audio
sig, sr = librosa.load(os.path.join(audio_path, audio_name),
                       sr=16000)
start = 1
duration = 5
sig = sig[int(start * sr) : int((start + duration) * sr)]  #時間區段
audio1 = Wav(sig, sr, '晨間霧水滴落在葉子的聲音(1s~6s)')
audio1.Mel_spec()
plt.show()

######################################## 濾波器 #######################################################

# sig2 = filter(sig, sr, fx=1024, mode='highpass')
# audio2 = Wav(sig2[int(1.8 * sr):], sr, '濾波' + audio_name)

################################### data augmentation #################################################
## 對聲音進行擴增

# Time Stretch(時間尺度變換)
# sig_ts = librosa.effects.time_stretch(sig, rate=0.8)  # rate > 1 加速，rate < 1 減速
# ts = Wav(sig_ts, sr, 'Time Stretch')
# ts.Mel_spec()

# Pitch Shift(音高尺度變換)
# sig_ps = librosa.effects.pitch_shift(sig, sr, n_steps=24)  # n_steps控制音調變化尺度
# ps = Wav(sig_ps, sr, 'Pitch Shift')
# ps.Mel_spec()

##對頻譜圖進行擴增
# audio.Mel_spec(augment=True,
#                time_warping_para=0,
#                frequency_masking_para=10,
#                time_masking_para=10,
#                frequency_mask_num=2,
#                time_mask_num=0)

#######################################################################################################


# audio2.Mel_spec()


######################################## 輸出wav ######################################################

# sf.write(os.path.join(audio_path, '濾波.wav'), sig2, sr)

# %%
