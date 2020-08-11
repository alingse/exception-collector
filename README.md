# exception-collector
python exception collector


## 目标

无痛地收集程序运行中产生的 Exception

不需要 logging.error() 也不需要 sentry

```python
try:
    raise ValueError('hello')
except Exception as e:
    pass
```

## demo

python3 demo.py

```

```