# CalculatorSupport v1.0

---

### Main API
- **calc_main**(expression: str, _format=True)  
计算表达式, expression表达式, _format启用语法糖  
- calc_format(expression: str):  
语法糖解释函数  
- precedence  
优先级存储  
precedence.build(precedence: list)构造优先级  
precedence.get(self, cls) -> int | None:获取操作符优先级  
### Main Property
- DefaultCalcType  
全局主类型设置, 默认为decimal  
- decimal_context高精小数设置    
decimal_context.prec 全局精度(单位:小数点后的位数)  
