import matplotlib.pyplot as plt
import numpy as np

def main():
    x_line = np.linspace(0.1, 5, 100)  #Генерирует массив из ровно 100 чисел, равномерно распределенных от 0.1 до 5
    x_int = np.arange(1, 6) #Создает массив целых чисел от 1 до 5
    
    plt.figure(figsize=(10, 6)) #Создает пустое окно
    
    plt.plot(x_line, x_line**2, color='blue', label='$x^2$')
    plt.plot(x_int, x_int**2, color='blue', marker='o', linestyle='None', markersize=8)
    
    plt.plot(x_line, np.exp(x_line), color='red', label='$e^x$')
    plt.plot(x_int, np.exp(x_int), color='red', marker='x', linestyle='None', markersize=8)
    
    plt.plot(x_line, np.log(x_line), color='green', label='$\ln(x)$')
    plt.plot(x_int, np.log(x_int), color='green', marker='s', linestyle='None', markersize=8)
    
    plt.plot(x_line, x_line**3, color='purple', label='$x^3$')
    plt.plot(x_int, x_int**3, color='purple', marker='^', linestyle='None', markersize=8)
    
    plt.title("Графики математических функций")
    plt.xlabel("Ось X")
    plt.ylabel("Ось Y")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.ylim(-5, 60)
    plt.xlim(0, 5.5)

   
main()
plt.show()