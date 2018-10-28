def test_add_liquidity(w3, custom_OMG_token, exchange_factory, custom_OMG_exchange, pad_bytes32):
    assert custom_OMG_exchange.name() == pad_bytes32('Uniswap V1')
    assert custom_OMG_exchange.symbol() == pad_bytes32('UNI-V1')
    assert custom_OMG_exchange.decimals() == 18
    assert custom_OMG_exchange.totalSupply() == 0
    assert custom_OMG_exchange.tokenAddress() == custom_OMG_token.address
    assert custom_OMG_exchange.factoryAddress() == exchange_factory.address
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 0
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 0
    a0, a1, a2 = w3.eth.accounts[:3]
    deadline = w3.eth.getBlock(w3.eth.blockNumber).timestamp + 300
    assert custom_OMG_exchange.tokenAddress() == custom_OMG_token.address
    assert custom_OMG_exchange.factoryAddress() == exchange_factory.address
    custom_OMG_token.approve(custom_OMG_exchange.address, 100*10**18, transact={})
    # # Can't add liquidity without tokens
    # assert_tx_failed(lambda: custom_OMG_exchange.addLiquidity(10*10**18, deadline, value=5*10**18, sender=t.k1))
    # # msg.value can't be 0
    # assert_tx_failed(lambda: custom_OMG_exchange.addLiquidity(10*10**18, deadline))
    # # Token value can't be 0
    # assert_tx_failed(lambda: custom_OMG_exchange.addLiquidity(0, deadline, value=5*10**18))
    # # Throw exception if not enough gas is provided
    # assert_tx_failed(lambda: custom_OMG_exchange.addLiquidity(10*10**18, deadline, value=5*10**18, startgas=25000))
    # Liquidity provider (t.a0) adds liquidity
    custom_OMG_exchange.addLiquidity(0, 10*10**18, deadline, transact={'value': 5*10**18})
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 5*10**18
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 10*10**18
    assert custom_OMG_exchange.totalSupply() == 5*10**18
    assert custom_OMG_exchange.balanceOf(a0) == 5*10**18

def test_liquidity_pool(w3, custom_OMG_token, exchange_factory, custom_OMG_exchange):
    a0, a1, a2 = w3.eth.accounts[:3]
    deadline = w3.eth.getBlock(w3.eth.blockNumber).timestamp + 300
    custom_OMG_token.transfer(a1, 10*10**18 + 1, transact={})
    custom_OMG_token.approve(custom_OMG_exchange.address, 100*10**18, transact={})
    custom_OMG_token.approve(custom_OMG_exchange.address, 10*10**18 + 1, transact={'from': a1})
    # First liquidity provider (t.a0) adds liquidity
    custom_OMG_exchange.addLiquidity(1, 2*10**18, deadline, transact={'value': 1*10**18})
    assert custom_OMG_exchange.totalSupply() == 1*10**18
    assert custom_OMG_exchange.balanceOf(a0) == 1*10**18
    assert custom_OMG_exchange.balanceOf(a1) == 0
    assert custom_OMG_exchange.balanceOf(a2) == 0
    assert custom_OMG_token.balanceOf(a1) == 10*10**18 + 1
    assert custom_OMG_token.balanceOf(a2) == 0
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 1*10**18
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 2*10**18
    # Second liquidity provider (a1) adds liquidity
    custom_OMG_exchange.addLiquidity(1, 11*10**18, deadline, transact={'value': 5*10**18, 'from': a1})
    assert custom_OMG_exchange.totalSupply() == 6*10**18
    assert custom_OMG_exchange.balanceOf(a0) == 1*10**18
    assert custom_OMG_exchange.balanceOf(a1) == 5*10**18
    assert custom_OMG_exchange.balanceOf(a2) == 0
    assert custom_OMG_token.balanceOf(a1) == 0
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 6*10**18
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 12*10**18 + 1
    # # Can't divest more liquidity than owned
    # assert_tx_failed(lambda: custom_OMG_exchange.removeLiquidity((5*10**18 + 1), 1, 1, deadline, transact={'from': a2})
    # Second liquidity provider (a1) transfers liquidity to third liquidity provider (a2)
    custom_OMG_exchange.transfer(a2, 2*10**18, transact={'from': a1})
    assert custom_OMG_exchange.balanceOf(a0) == 1*10**18
    assert custom_OMG_exchange.balanceOf(a1) == 3*10**18
    assert custom_OMG_exchange.balanceOf(a2) == 2*10**18
    assert custom_OMG_token.balanceOf(a1) == 0
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 6*10**18
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 12*10**18 + 1
    # First, second and third liquidity providers remove their remaining liquidity
    custom_OMG_exchange.removeLiquidity(1*10**18, 1, 1, deadline, transact={})
    custom_OMG_exchange.removeLiquidity(3*10**18, 1, 1, deadline, transact={'from': a1})
    custom_OMG_exchange.removeLiquidity(2*10**18, 1, 1, deadline, transact={'from': a2})
    assert custom_OMG_exchange.totalSupply() == 0
    assert custom_OMG_exchange.balanceOf(a0) == 0
    assert custom_OMG_exchange.balanceOf(a1) == 0
    assert custom_OMG_exchange.balanceOf(a2) == 0
    assert custom_OMG_token.balanceOf(a1) == 6*10**18
    assert custom_OMG_token.balanceOf(a2) == 4*10**18 + 1
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 0
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 0
    # Can add liquidity again after all liquidity is divested
    custom_OMG_exchange.addLiquidity(0, 2*10**18, deadline, transact={'value': 1*10**18})
