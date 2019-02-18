def build(self):
            end_time = timeit.default_timer()
            end_mem = memory_profiler.memory_usage()[0]

            sys.stdout = self._previous_stdout

            self._log.write("END RequestId: {r}\n".format(
                r=self._context.aws_request_id))

            duration_in_millis = int(math.ceil(1000 * (end_time - self._start_time)))
            # The memory overhead of setting up the AWS Lambda environment
            # (when actually run in AWS) is roughly 14 MB
            max_memory_used_in_mb = (end_mem - self._start_mem) / 1048576 + 14

            self._log.write(
                "REPORT RequestId: {r}\tDuration: {d} ms\t"
                "Max Memory Used: {m} MB\n"
                .format(r=self._context.aws_request_id,
                        d=duration_in_millis,
                        m=max_memory_used_in_mb))

            log = self._log.getvalue()
            return LambdaCallSummary(duration_in_millis, max_memory_used_in_mb, log) 

def test_memory_usage_ok():
    import memory_profiler
    dataset = ReplayPool(
        observation_shape=(80, 80),
        action_dim=1,
        max_steps=100000,
        concat_observations=True,
        concat_length=4
    )
    last = time.time()

    for i in range(1000000000):
        if (i % 100000) == 0:
            print(i)
        dataset.add_sample(np.random.random((80, 80)), 1, 1, False)
        if i > 200000:
            dataset.random_batch(32)
        if (i % 10007) == 0:
            print(time.time() - last)
            mem_usage = memory_profiler.memory_usage(-1)
            print(len(dataset), mem_usage)
        last = time.time() 

def test_memory_usage_ok():
    import memory_profiler
    dataset = ReplayPool(
        observation_shape=(80, 80),
        action_dim=1,
        max_steps=100000,
        concat_observations=True,
        concat_length=4
    )
    last = time.time()

    for i in range(1000000000):
        if (i % 100000) == 0:
            print(i)
        dataset.add_sample(np.random.random((80, 80)), 1, 1, False)
        if i > 200000:
            dataset.random_batch(32)
        if (i % 10007) == 0:
            print(time.time() - last)
            mem_usage = memory_profiler.memory_usage(-1)
            print(len(dataset), mem_usage)
        last = time.time() 

def test_main():
    min_kb, max_kb = get_bounds()

    # This should be the **only** test function here.
    gc.disable()
    intersect_all()
    kb_used_after = memory_profiler.memory_usage(max_usage=True)
    if min_kb <= kb_used_after <= max_kb:
        status = 0
        msg = SUCCESS_TEMPLATE.format(kb_used_after)
        print(msg)
    else:
        status = 1
        msg = ERR_TEMPLATE.format(kb_used_after, min_kb, max_kb)
        print(msg, file=sys.stderr)

    gc.enable()
    sys.exit(status) 

def test_main():
    min_kb, max_kb = get_bounds()

    # This should be the **only** test function here.
    gc.disable()
    intersect_all()
    kb_used_after = memory_profiler.memory_usage(max_usage=True)
    if min_kb <= kb_used_after <= max_kb:
        status = 0
        msg = SUCCESS_TEMPLATE.format(kb_used_after)
        print(msg)
    else:
        status = 1
        msg = ERR_TEMPLATE.format(kb_used_after, min_kb, max_kb)
        print(msg, file=sys.stderr)

    gc.enable()
    sys.exit(status) 

def test_memory_usage_ok():
    import memory_profiler
    dataset = ReplayPool(
        observation_shape=(80, 80),
        action_dim=1,
        max_steps=100000,
        concat_observations=True,
        concat_length=4
    )
    last = time.time()

    for i in range(1000000000):
        if (i % 100000) == 0:
            print(i)
        dataset.add_sample(np.random.random((80, 80)), 1, 1, False)
        if i > 200000:
            dataset.random_batch(32)
        if (i % 10007) == 0:
            print(time.time() - last)
            mem_usage = memory_profiler.memory_usage(-1)
            print(len(dataset), mem_usage)
        last = time.time() 