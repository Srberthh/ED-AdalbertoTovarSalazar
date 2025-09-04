internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("--¿El numero es primo?--");

        int intNumero = 0;
        bool blnEntradaValida = false;

        while (!blnEntradaValida)
        {
            Console.Write("Teclee un numero: ");

            try
            {
                intNumero = Convert.ToInt32(Console.ReadLine());
                blnEntradaValida = true;
            }
            catch (FormatException)
            {
                Console.WriteLine("Error: Ingrese solo datos numericos. Intente de nuevo.");
            }
            catch (OverflowException)
            {
                Console.WriteLine("Error: El numero es demasiado grande. Intente de nuevo.");
            }
        }

        if (intNumero % 2 == 0)
        {
            Console.WriteLine($"{intNumero} es un numero Primo");
        }
        else
        {
            Console.WriteLine($"{intNumero} no es un numero Primo");
        }

        Console.ReadKey();

    }
}