# Fazer um programa para ler o valor "r" do raio de um círculo, e depois mostrar o valor da área do
# círculo com três casas decimais. A fórmula da área do círculo é a seguinte: 𝑎𝑟𝑒𝑎 = 𝜋. 𝑟􀬶. Você pode
# usar o valor de 𝜋 fornecido pela biblioteca da sua linguagem de programação, ou então, se preferir, use
# diretamente o valor 3.14159.


circleRadius = float(input("Enter the radius of circle : "))
circleArea = 3.14159*(circleRadius**2)

print(f"The area of circle is : {circleArea:.6f} ")
