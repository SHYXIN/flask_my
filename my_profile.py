import pstats

# 替换成你想分析的 .prof 文件路径
profile_file = './profiles/GET.auth.login.000007ms.1721630268.prof'

p = pstats.Stats(profile_file)
p.strip_dirs().sort_stats('cumulative').print_stats(50)
