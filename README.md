This is a diagram of the [xSDK](https://xsdk.info).

To get an updated graph, use [Spack](https://github.com/spack/spack):

```
spack graph --dot xsdk > xsdk.dot
```

You can then edit the `.dot` file to look more like the ones here.

To produce the properly colored graph to match previous xSDK graphs,
you will need to apply the spack-graph-xsdk.patch to your spack
installation before running the ``spack graph`` command.

To edit the `.graffle` file, you need
[Omnigraffle](https://www.omnigroup.com/omnigraffle).
