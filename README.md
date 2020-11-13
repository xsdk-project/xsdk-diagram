This is a diagram of the [xSDK](https://xsdk.info).

To get an updated graph, use [Spack](https://github.com/spack/spack):

```
spack graph -d xsdk+cuda ^openblas@0.3.5 ^hwloc@1.999 ^magma cuda_arch=60 > xsdk.dot

egrep -v '(yscpz2kynmdxjogx62xwwvhmmqmvfhsy|...)' xsdk.dot > xsdk.dot

# <edit xsdk.dot, update header and colors>
echo "$(./color_graph.py xsdk.dot)" > xsdk.dot

dot -Tpdf xsdk.dot  > xsdk.pdf

convert xsdk.pdf xsdk.jpg

```
