defmodule MyModule.Loop do
  def multiplier(m) do
    multiplier(m, 1)
  end

  defp multiplier(_, 11), do: nil

  defp multiplier(prod1, prod2) do
    IO.puts("#{prod1} x #{prod2} = #{prod1 * prod2}")
    multiplier(prod1, prod2 + 1)
  end
end
