import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from arrow3D import Arrow3D


def get_angle(x, y):
    if x == 0 and y == 0:
        return 0
    return np.rad2deg(np.arccos(x/np.sqrt(x**2+y**2)))


def get_initial_values():

    def _try():

        def is_number():
            nonlocal x
            try:
                float(x)
                return True
            except ValueError:
                return False

        x = input()
        # if x == '0':
        #     x = float(x)
        if is_number():
            return float(x)
        print("Введено не число, введите число\n")
        return _try()

    print('Введите начальные значения\nVx = ')
    Vx = _try()
    print('Vy = ')
    Vy = _try()
    print('Vz = ')
    Vz = _try()
    print('Ex = ')
    Ex = _try()
    print('Ey = ')
    Ey = _try()
    print('Bx = ')
    Bx = _try()
    return Vx, Vy, Vz, Ex, Ey, Bx


def main():
    # СГС
    # Vx0 = 1
    # Vy0 = 1
    # Vz0 = 1
    # Ex = .5  # Тл
    # Bx = .5  # Тл
    # Ey = .5  # Тл

    # СГС
    q = 1#-4.8e-10  # −4,80320427(13)·10−10 ед. заряда СГСЭ
    m = 1#9.1e-28  # 9,10938356(11)·10−28 грамм
    c = 1#3e10  # 2,99792458*1010 см/с
    #
    pause = False

    def onKey(event):
        onClick(event)

    def onClick(event):
        nonlocal anim_running
        if anim_running:
            ani.event_source.stop()
            anim_running = False
            print('paused')
        else:
            ani.event_source.start()
            anim_running = True
            print('unpaused')

    def init():
        mpl.rcParams['legend.fontsize'] = 10

    # обработка кадра
    def data(i, t, line):
        global ani
        if pause:
            ani.event_source.stop()

        t += 1e-3*i
        x = Vx0 * t + C1 * t ** 2
        y = C2 * np.cos(C3 * t) + C4 * np.sin(C3 * t)
        z = -C2 * np.sin(C3 * t) - C4 * np.cos(C3 * t) - C5 * t
        print(x[0], y[0], z[0])

        line = ax.plot(x, y, z, color='b')
        return line

    # инициализация
    init()
    Vx0, Vy0, Vz0, Ex, Ey, Bx = get_initial_values()
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.set_xlabel("Oсь X")
    ax.set_ylabel("Oсь Y")
    ax.set_zlabel("Ocь Z")
    arrowB = Arrow3D([0, 20*Bx], [0, 0], [0, 0], mutation_scale=20, lw=1, arrowstyle="-|>", color="g")
    arrowE = Arrow3D([0, 4*Ex], [0, 4*Ey], [0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="r")
    ax.add_artist(arrowB)
    ax.add_artist(arrowE)

    angle =int(get_angle(Ex, Ey))
    ax.set_title("Движение электрона в полях E и B\n B || OZ, [B x E] || OZ\nМежду B и E {} градусов".format(angle))

    fig.canvas.mpl_connect('key_press_event', onKey)

    # вычисление констант
    C1 = q/(m*2)*Ex
    C2 = m*c*(Vz0+(Ey/Bx)*c)/(q*Bx)
    C3 = q*Bx/(m*c)
    C4 = Vy0*m*c/(q*Bx)
    C5 = Ey*c/Bx

    t = np.linspace(0, 1, 400)
    x = Vx0*t + C1*t**2
    y = C2*np.cos(C3*t) + C4*np.sin(C3*t)
    z = -C2*np.sin(C3*t) - C4*np.cos(C3*t) - C5*t

    # построение анимации
    line = ax.plot(x, y, z, color='b')
    anim_running = True
    ani = animation.FuncAnimation(fig, data, fargs=(t, line), interval=100)

    plt.show()


def vanya():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    t = np.linspace(0, 1, 2)



if __name__ == '__main__':

    main()