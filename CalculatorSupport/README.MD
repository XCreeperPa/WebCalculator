# CalculatorSupport v1.0

---

### Main API

- **calc_main**(expression: str, _format=True)  
  *计算表达式, expression表达式, _format启用语法糖*
- calc_format(expression: str):  
  *语法糖处理*
- log: Logger.Logger  
  *calc_main日志, 默认为print输出到控制台*
    - log(message): 记录日志消息
    - setIO(output=None): 设置或重置输出流对象, 如果没有指定output，则返回默认的 `print` 输出
    - currentIO(): 获取当前的输出流对象, 如果没有指定输出流对象，则返回None
    - create_string_io(): 创建自定义内存输出流实例
    - create_file_io(self, file: str, mode: str = 'w', encoding: str = None, newline: str = None): 创建自定义文件输出流实例
    - read(): 读取日志默认IO, 类似于`log.currentIO().read()`, 但是每次只返回更新的部分

- operator_precedence: OperatorPrecedence.OperatorPrecedence  
  *运算符优先级存储*  
  operator_precedence.build(precedence: list)构造优先级  
  operator_precedence.get(self, cls) -> int | None:获取操作符优先级

### Main Property

- DefaultCalcType  
  全局主类型设置, 默认为decimal
- decimal_context高精小数设置  
  decimal_context.prec = 30 全局精度(单位:小数点后的位数)

### Example

```python
from CalculatorSupport import calc_main, log

io = log.create_string_io()
result = calc_main("1+1")
print(log.read())
# print(io.read())
print(log.readlines())
print(log.readline())
```