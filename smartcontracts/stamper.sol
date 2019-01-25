pragma solidity ^0.5.0;

/**
    @title Smart contract for Proff of Existence
*/
contract Stamper {
    event Stamped(address indexed from, string indexed hash, string indexed ots);

    event Deploy(address indexed from);
    event SelfDestroy(address indexed from);

    struct Data {
        uint blockNumber;
        string hash;
    }
    mapping (string => Data) private hashstore;
    address payable owner;

    constructor() public {
        owner = msg.sender;
        emit Deploy(msg.sender);
    }

    function stamp(string memory ots, string memory file_hash) public {
        if (hashstore[ots].blockNumber == 0) {
            emit Stamped(msg.sender, file_hash, ots);
            hashstore[ots] = Data({blockNumber: block.number, hash: file_hash});
        }
    }

    function verify(string memory ots, string memory file_hash) public view returns(bool){
        Data memory data = hashstore[ots];
        return stringsEqual(data.hash, file_hash);
    }

    function getHash(string memory ots) public view returns(string memory){
        Data memory data = hashstore[ots];
        return data.hash;
    }

    function getBlockNumber(string memory ots) public view returns(uint){
        Data memory data = hashstore[ots];
        return data.blockNumber;
    }

    function stringsEqual(string memory _a, string memory _b) internal pure returns (bool) {
        bytes memory a = bytes(_a);
        bytes memory b = bytes(_b);

        if (keccak256(a) != keccak256(b)) { return false; }
        return true;
    }

    function selfDestroy() public{
        require(msg.sender == owner);
        emit SelfDestroy(msg.sender);
        selfdestruct(owner);
    }
}