


from fastmcp import FastMCP
import random

mcp = FastMCP(name="Demo Server")

@mcp.tool
def roll_dice(n_dice: int=1) -> list[int]:
    "roll a n_dice 6-Sided and return the results"
    return [random.randint(1,6) for _ in range(n_dice)]

@mcp.tool
def add_numbers(a:float,b:float) ->float:
      " give the addition of the two numbers"
      return a +b

@mcp.tool
def mul_num(c:float, d:float) -> float:
      "give the multiplication  of the two numbers"
      return c * d

@mcp.tool
def sub_num(e:float, f:float) -> float:
      "give the subraction  of the two numbers"
      return e - f

@mcp.tool
def pow_num(g:float, h:float) -> float:
      "give the pow  of the two numbers"
      return g**h

if __name__=="__main__":
        mcp.run()



