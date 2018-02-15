for i in {1,2,3}; do robot --name hello$i -o outdir$i/out$i.xml hello.robot; done

rebot --name hellos outdir*/*xml
