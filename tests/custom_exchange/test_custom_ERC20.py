def test_ERC20(w3, custom_OMG_token, pad_bytes32):
    a0, a1 = w3.eth.accounts[:2]
    assert custom_OMG_token.name() == pad_bytes32('OMG Token')
    assert custom_OMG_token.symbol() == pad_bytes32('OMG')
    assert custom_OMG_token.decimals() == 18
    assert custom_OMG_token.totalSupply() == 100000*10**18
    assert custom_OMG_token.balanceOf(a0) == 100000*10**18
    custom_OMG_token.transfer(a1, 1*10**18, transact={})
    assert custom_OMG_token.balanceOf(a0) == 100000*10**18 - 1*10**18
    assert custom_OMG_token.balanceOf(a1) == 1*10**18
