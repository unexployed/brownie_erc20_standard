from brownie import OurToken
from scripts.utils import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")

def deploy():
    deployer = get_account()
    toucan = OurToken.deploy(initial_supply, {"from" : deployer})
    print(f"{toucan.balanceOf(deployer.address)}")


def main():
    deploy()