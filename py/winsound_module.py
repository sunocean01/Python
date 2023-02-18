'''winsound'''
import winsound


'''winsound(frequency,duration)'''
# winsound.Beep(1000,1000)


'''winsound.MessageBeep(winsound.xxx): 从Platform API 调用基础 MessageBeep（）函数
xxx: -1，MB_ICONASTERISK，MB_ICONEXCLAMATION，MB_ICONHAND，MB_ICONQUESTION和MB_OK'''

# winsound.MessageBeep(winsound.MB_ICONASTERISK)

# exit()

'''检测文档中的possible sounds 哪些是你电脑的messageBeep'''
def play(): 
    sounds=["-1","winsound.MB_ICONASTERISK","winsound.MB_ICONEXCLAMATION","winsound.MB_ICONHAND","winsound.MB_ICONQUESTION","winsound.MB_OK"]
    for i in sounds:
        try:
            winsound.MessageBeep(eval(i))
        except RuntimeError and NameError:
            print("no {} messagebeep".format(i))
        else:
            print("has the sound flag{}".format(i))
# play()



'''winsound.PlaySound(sound, flags),从平台API 调用底层函数。声音参数可以是文件名，音频数据作为一个字符串，或None'''
'''
sound 系统内置声音:
    'SystemAsterisk'    Asterisk
    'SystemExclamation'    Exclamation
    'SystemExit'    Exit Windows
    'SystemHand'    Critical Stop
    'SystemQuestion'    Question
flags:
    winsound.SND_ALIAS  该声音参数是从注册表中声音的关联名称。如果注册表中不包含此类名称，则除非SND_NODEFAULT另外指定，否则请播放系统默认声音。如果没有登录默认声音，请提高RuntimeError。不要与指定的'wav格式文件一起使用。
    winsound.SND_LOOP   反复播放声音。该SND_ASYNC标志也必须用于避免阻塞。不能用于SND_MEMORY。
    winsound.SND_MEMORY 声音参数PlaySound()是WAV文件的存储器中的图像，为一个字符串。注意这个模块不支持异步播放内存映像，所以这个标志的组合SND_ASYNC将会提升RuntimeError
    winsound.SND_PURGE  停止播放指定声音的所有实例。注意现代Windows平台不支持此标志。
    winsound.SND_ASYNC  立即返回，允许声音异步播放。
    winsound.SND_NODEFAULT  如果找不到指定的声音，请不要播放系统默认声音。
    winsound.SND_NOSTOP 不要中断当前播放的声音。
    winsound.SND_NOWAIT 如果声音驱动程序正忙，请立即返回。注意现代Windows平台不支持此标志。
    winsound.MB_ICONASTERISK    播放SystemDefault声音。
    winsound.MB_ICONEXCLAMATION  播放SystemExclamation声音。
    winsound.MB_ICONHAND    播放SystemHand声音。
    winsound.MB_ICONQUESTION    播放SystemQuestion声音。
    winsound.MB_OK  播放SystemDefault声音。
'''

winsound.PlaySound(r'.\testfile\qianmenqingsidawancha.wav',winsound.SND_LOOP)
# winsound.PlaySound('SystemExit',winsound.SND_ALIAS)