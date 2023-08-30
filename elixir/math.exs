defmodule MyModule.Math do
  def sum(number1, number2) do
    number1 + number2
  end

  def zero?(0), do: true
  def zero?(x) when (is_integer), do: false
end
