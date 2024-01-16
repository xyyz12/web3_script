# web3_script
主要在于合约交互，参考别人写，直到自己会写，做个记录

代码参考：https://github.com/JetCyC/web3_script_tutorial 

教程参考：https://mirror.xyz/gm365.eth/ad4vbp_qLFKaOrAMtE2YZ6pzMuC3ejam-y_62QogSds


1、连接到以太节点

![image](https://github.com/xyyz12/web3_script/assets/91812763/f7dc5d58-a311-49cf-8311-8e4d22def04f)


![image](https://github.com/xyyz12/web3_script/assets/91812763/02132dea-8735-4391-8e13-3044a6237c15)


![image](https://github.com/xyyz12/web3_script/assets/91812763/8579433d-131e-42d1-919e-b2dab6e640b9)


![image](https://github.com/xyyz12/web3_script/assets/91812763/71729581-3564-4ded-8189-f1a82df9be8a)


之后，就可进行查询链上数据，还是进行转账、合约交互

2、转帐就相当于发送交易（sending transactions）

![image](https://github.com/xyyz12/web3_script/assets/91812763/5304f6ba-88ba-4cdb-9553-f01a22f5bce8)


![image](https://github.com/xyyz12/web3_script/assets/91812763/6a72076e-09e0-41c4-a0cd-aee69735d9fa)


通过函数包装了一下交易


3、验证是否与节点连接

![image](https://github.com/xyyz12/web3_script/assets/91812763/83a1dea3-6d6e-4dcd-b48d-38d1645c7f4e)

4、函数实例化来完成这个操作
![image](https://github.com/xyyz12/web3_script/assets/91812763/cd1a3d5f-3333-4949-9cca-1876c20c6bab)


donate:0x43C1CfB2F164251fc9b6c958b64485D2b94870C4



1、确定合约地址

先在xxxx官方跨链桥测试网页面手工交互

接着从交互记录，找到 Etherscan上合约地址

2、获取合约ABI

![image](https://github.com/xyyz12/web3_script/assets/91812763/020126b2-43d8-443a-a45f-10078c1739cf)

![image](https://github.com/xyyz12/web3_script/assets/91812763/1e55c0f0-adc8-4567-9797-54374c3646bc)


![image](https://github.com/xyyz12/web3_script/assets/91812763/4848f0d1-01f4-48ef-9d9b-723965005ab4)


![image](https://github.com/xyyz12/web3_script/assets/91812763/46f1c5ef-8a53-45bd-97be-43cd02981e6c)


3、研究函数名及参数具体含义

https://goerli.etherscan.io/address/0x0e9B63A28d26180DBf40E8c579af3aBf98aE05C5#writeProxyContract

![image](https://github.com/xyyz12/web3_script/assets/91812763/40d1c148-4400-47af-a92d-b75f0258f50f)

定位到合约 "Write Contract" 中的 “  ”，例子"depositEth" 函数，获取函数名称及对应参数，，，但是合约里啥都没有，，，幸好留下了abi，通过其它方式找函数名称呗
注：本例中其实是定位到 “Write As Proxy”的页面，说明当前合约是一个可升级合约

看完abi发现，信息不全，在网站 chunk-vendor-xxx.js 文件中定位到了完整的 ABI 信息。
找的途径

1、去github上找代码，在各类js文件中搜”abi”

2、解析4字节函数选择器

3、搜索网页源码的abi信息

![image](https://github.com/xyyz12/web3_script/assets/91812763/3c774bbe-afa7-436d-b70b-965c1d4b3132)


4、写交互代码，广播交易信息

![1c7c447ce0e5a665bf0a0fa5515a56d](https://github.com/xyyz12/web3_script/assets/91812763/01d1a3c5-5f8a-46eb-bbaa-22bec2365197)

在inputdata 中看refuel转账模块的函数

![1705375649291](https://github.com/xyyz12/web3_script/assets/91812763/c932b68e-8583-4ae1-9100-11d995119c81)


通过depositnative这个函数实现了跨链



