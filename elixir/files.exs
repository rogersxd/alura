defmodule  MyModule.Files do
  def read_file(file) do
    case File.read(file) do
      {:ok, content} -> IO.puts(content)
      {:error, _} -> "Error!"
    end
  end

  def write_file() do
    file = File.open("file2.txt", [:write, :utf8])
    IO.write(elem(file, 1), "test!2")
    File.close(elem(file, 2))
  end
end
