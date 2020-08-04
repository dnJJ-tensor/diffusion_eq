import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import japanize_matplotlib
import heat_Euler


#function which make 2Dconter map
def Conter(l1, l2, n1, n2, z, ttl):
    x1 = np.linspace(0, l1, n1)
    x2 = np.linspace(0, l2, n2)
 
    X1, X2 = np.meshgrid(x1, x2)

    fig = plt.figure()   

    
    plt.contourf(X1, X2, z, cmap = 'jet')
    
    #以下のコマンドを追加すると、アスペクト比が揃う
    #plt.gca().set_aspect('equal')
    plt.title(ttl)
    plt.show()
    fig.savefig("result/T_in{}step_2d.png".format(ttl))
    
    return  

#function which make 3d figure
def SurFace(l1, l2, n1, n2, z, ttl):
    #make grid
    x1 = np.linspace(0, l1, n1)
    x2 = np.linspace(0, l2, n2)
 
    X1, X2 = np.meshgrid(x1, x2)

    fig = plt.figure() 

    ax = fig.add_subplot(111, projection='3d')

    ax.set_title("3d plot of {} times iteration".format(ttl))

    ax.plot_surface(X1, X2, z, cmap = 'jet')

    plt.show()
    fig.savefig("result/T_in{}step_3d.png".format(ttl))

    return



#Read CSV file which indicate initial condition
#fileの名前
filename = 'Tinit_test.csv'
df_Tinit = pd.read_csv("data/{}".format(filename), header = None )


#dataframeを数値計算ができるようにnumpy.arrayに変換
#初期温度分布をTinit
#結果のプロットにはTinout
Tinit    = np.array(df_Tinit)
Tinout = np.array(df_Tinit)

#第一引数がxの要素数.第二引数がyの要素数
nx, ny = Tinit.shape
print(nx, ny)

#シミュレーションに必要な各種パラメータの設定
lx = 1
ly = 1
kappa = 0.0040
dt = 0.0060
dx = lx / (nx - 1)
dy = ly / (ny - 1)

#Euler法の収束判定.収束するならばシミュレーションを実行
DX = kappa*dt/(dx**2)
DY = kappa*dt/(dy**2)
if (DX + DY <= 0.50):
    #number of iteration
    itrnum = 300
    for itr in range(1, itrnum+1):
        Tinout = heat_Euler.twodscalor_euler_explc(Tinout, DX, DY, nx, ny)
        
    Conter(lx,ly, nx, ny, Tinout, '{}'.format(itrnum))
    SurFace(lx,ly, nx, ny, Tinout, '{}'.format(itrnum))
    #分布図を保存
    np.savetxt('data/Result_in_{}step.csv'.format(itrnum),Tinout,delimiter=',')

#パラメータが収束条件を満たさないとき  
else :
    print(DX+DY)
    print("Reset parameter to converge answer.")  
