def test_swap_input(w3, custom_OMG_token, custom_OMG_exchange):
    a0, a1, a2 = w3.eth.accounts[:3]
    deadline = w3.eth.getBlock(w3.eth.blockNumber).timestamp + 300
    custom_OMG_token.transfer(a1, 2*10**18, transact={})
    custom_OMG_token.approve(custom_OMG_exchange.address, 10*10**18, transact={})
    custom_OMG_token.approve(custom_OMG_exchange.address, 2*10**18, transact={'from': a1})
    custom_OMG_exchange.addLiquidity(0, 10*10**18, deadline, transact={'value': 5*10**18})
    # Starting balances of UNI exchange
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 5*10**18
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 10*10**18
    # Starting balances of BUYER
    assert custom_OMG_token.balanceOf(a1) == 2*10**18
    assert w3.eth.getBalance(a1) == 1*10**24
    # BUYER converts ETH to UNI
    custom_OMG_exchange.tokenToEthSwapInput(2*10**18, 1, deadline, transact={'from': a1})
    # Updated balances of UNI exchange
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 4168751042187760547
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 12*10**18
    # Updated balances of BUYER
    assert custom_OMG_token.balanceOf(a1) == 0
    assert w3.eth.getBalance(a1) == 1*10**24 + 831248957812239453

def test_transfer_input(w3, custom_OMG_token, custom_OMG_exchange):
    a0, a1, a2 = w3.eth.accounts[:3]
    deadline = w3.eth.getBlock(w3.eth.blockNumber).timestamp + 300
    custom_OMG_token.transfer(a1, 2*10**18, transact={})
    custom_OMG_token.approve(custom_OMG_exchange.address, 10*10**18, transact={})
    custom_OMG_token.approve(custom_OMG_exchange.address, 2*10**18, transact={'from': a1})
    custom_OMG_exchange.addLiquidity(0, 10*10**18, deadline, transact={'value': 5*10**18})
    # Starting balances of UNI exchange
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 5*10**18
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 10*10**18
    # Starting balances of BUYER
    assert custom_OMG_token.balanceOf(a1) == 2*10**18
    assert w3.eth.getBalance(a1) == 1*10**24
    # Starting balances of RECIPIENT
    assert custom_OMG_token.balanceOf(a2) == 0
    assert w3.eth.getBalance(a2) == 1*10**24
    # BUYER converts ETH to UNI
    custom_OMG_exchange.tokenToEthTransferInput(2*10**18, 1, deadline, a2, transact={'from': a1})
    # Updated balances of UNI exchange
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 4168751042187760547
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 12*10**18
    # Updated balances of BUYER
    assert custom_OMG_token.balanceOf(a1) == 0
    assert w3.eth.getBalance(a1) == 1*10**24
    # Updated balances of RECIPIENT
    assert custom_OMG_token.balanceOf(a2) == 0
    assert w3.eth.getBalance(a2) == 1*10**24 + 831248957812239453

def test_swap_output(w3, custom_OMG_token, custom_OMG_exchange):
    a0, a1, a2 = w3.eth.accounts[:3]
    deadline = w3.eth.getBlock(w3.eth.blockNumber).timestamp + 300
    custom_OMG_token.transfer(a1, 3*10**18, transact={})
    custom_OMG_token.approve(custom_OMG_exchange.address, 10*10**18, transact={})
    custom_OMG_token.approve(custom_OMG_exchange.address, 3*10**18, transact={'from': a1})
    custom_OMG_exchange.addLiquidity(0, 10*10**18, deadline, transact={'value': 5*10**18})
    # Starting balances of UNI exchange
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 5*10**18
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 10*10**18
    # Starting balances of BUYER
    assert custom_OMG_token.balanceOf(a1) == 3*10**18
    assert w3.eth.getBalance(a1) == 1*10**24
    # BUYER converts ETH to UNI
    custom_OMG_exchange.tokenToEthSwapOutput(831248957812239453, 3*10**18, deadline, transact={'from': a1})
    # Updated balances of UNI exchange
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 4168751042187760547
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 12*10**18
    # Updated balances of BUYER
    assert custom_OMG_token.balanceOf(a1) == 1*10**18
    assert w3.eth.getBalance(a1) == 1*10**24 + 831248957812239453

def test_transfer_output(w3, custom_OMG_token, custom_OMG_exchange):
    a0, a1, a2 = w3.eth.accounts[:3]
    deadline = w3.eth.getBlock(w3.eth.blockNumber).timestamp + 300
    custom_OMG_token.transfer(a1, 3*10**18, transact={})
    custom_OMG_token.approve(custom_OMG_exchange.address, 10*10**18, transact={})
    custom_OMG_token.approve(custom_OMG_exchange.address, 3*10**18, transact={'from': a1})
    custom_OMG_exchange.addLiquidity(0, 10*10**18, deadline, transact={'value': 5*10**18})
    # Starting balances of UNI exchange
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 5*10**18
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 10*10**18
    # Starting balances of BUYER
    assert custom_OMG_token.balanceOf(a1) == 3*10**18
    assert w3.eth.getBalance(a1) == 1*10**24
    # Starting balances of RECIPIENT
    assert custom_OMG_token.balanceOf(a2) == 0
    assert w3.eth.getBalance(a2) == 1*10**24
    # BUYER converts ETH to UNI
    custom_OMG_exchange.tokenToEthTransferOutput(831248957812239453, 3*10**18, deadline, a2, transact={'from': a1})
    # Updated balances of UNI exchange
    assert w3.eth.getBalance(custom_OMG_exchange.address) == 4168751042187760547
    assert custom_OMG_token.balanceOf(custom_OMG_exchange.address) == 12*10**18
    # Updated balances of BUYER
    assert custom_OMG_token.balanceOf(a1) == 1*10**18
    assert w3.eth.getBalance(a1) == 1*10**24
    # Updated balances of RECIPIENT
    assert custom_OMG_token.balanceOf(a2) == 0
    assert w3.eth.getBalance(a2) == 1*10**24 + 831248957812239453
