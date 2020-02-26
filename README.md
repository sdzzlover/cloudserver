# cloudserver
云服务器上简单部署一个socket后台
注意几个问题，1，需要安全策略里开port 8000.
注意需要ip设置为 私有ip。
要读固定路径，我我的服务器上有/home/vinson/YOLOv3/，不然会报错，改为自己路径即可，这里面读取clinet发送过来的文件地址，我的地址+clinet发来的地址文件读取。
