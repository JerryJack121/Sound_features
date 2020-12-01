import os
import librosa
from wav_plot import Wav_plot
import matplotlib.pyplot as plt
from scipy import signal
import soundfile as sf


def main():
    audio_path = 'D:\DATASET\冷氣故障聲'
    audio_name = '國立臺北科技大學31.wav'

    # load audio
    sig, sr = librosa.load(os.path.join(audio_path, audio_name),
                           sr=40000,
                           duration=5)
    audio = Wav_plot(sig, sr, audio_name)
    # 初始化參數
    audio1 = Wav_plot(sig, sr, audio_name)

    ######################################## 濾波器 #######################################################

    fx = 1024  #濾波器頻率
    wn = 2 * fx / sr
    b, a = signal.butter(8, wn, 'highpass')  #配置濾波器 8 表示濾波器的階數
    sig2 = signal.filtfilt(b, a, sig)  #data為要過濾的訊號
    # 初始化參數
    audio2 = Wav_plot(sig2, sr, audio_name)

    ################################### data augmentation #################################################
    # 對聲音進行擴增

    # Time Stretch(時間尺度變換)
    sig_ts = librosa.effects.time_stretch(sig,
                                          rate=0.8)  # rate > 1 加速，rate < 1 減速
    ts = Wav_plot(sig_ts, sr, 'Time Stretch')
    # Pitch Shift
    sig_ps = librosa.effects.pitch_shift(sig, sr,
                                         n_steps=24)  # n_steps控制音調變化尺度
    ps = Wav_plot(sig_ps, sr, 'Pitch Shift')

    ####################################################################################################

    ## 畫圖
    audio1.Mel_spec(fmax=sr / 2)  #fmax跟採樣頻率有關，若fmax提高。採樣頻率也要提高，否則高頻會被切掉
    audio2.Mel_spec(fmax=sr / 2)
    # audio.frequence_wavform()
    # ts.Mel_spec(fmax=sr / 2)
    # ps.Mel_spec(fmax=sr / 2)
    # audio.Mel_spec(fmax=sr / 2, augment=True)
    plt.show()

    ######################################################################################################
    # 輸出wav
    # sf.write(os.path.join(audio_path, '濾波.wav'), sig2, sr)
    ####################################### 初始化參數 ####################################################


if __name__ == "__main__":
    main()