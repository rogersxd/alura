defmodule MyModule.Multiplier do
  def calc(multiplier) do
    multiply(multiplier, 1, [])
  end

  defp multiply(_, 11, values), do: values

  defp multiply(prod1, prod2, values) do
    multiply(prod1, prod2 + 1, [prod1 * prod2] ++ values)
  end
end
