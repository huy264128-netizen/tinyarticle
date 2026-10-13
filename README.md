## 便宜文章发布器
这是一个极其微型的文章发布工具,作用只有一个,就是把目录下的md转成html 然后发布在CF Pages上
当然,还是需要更改一些CF Page配置的
把构建命令修改为
```bash
./build.py
```
部署命令用
```bash
npx wrangler deploy
```
就行了

## 正确的打开方式
```bash
git clone https://github.com/huy264128-netizen/tinyarticle.git <你的文件目录>
cd <你的文件目录>
git remote set-url origin <你自己的仓库>
git push
```
然后在Cloudflare Pages上部署即可

注意构建命令用 `./build.py` 部署命令用 `npx wrangler deploy`
