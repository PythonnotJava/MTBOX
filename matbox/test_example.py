from MT import *
import sys

if __name__ == '__main__':
    app = ReAppication(sys.argv)
    ui = CoreUI(False)
    ui.setCard(text="""
    数据仓库的特点？
主题性
传统的数据库，更多的可能是考虑到应用层面上的数据组织和结构，因此各个业务之间的数据可能相互独立，相互分离。而数据仓库是对业务系统中各业务数据通过不同主题域特征进行抽象，通过归纳和总结等手段，形成一个更高层次的主题和维度抽象。

集成性
因为数据仓库与传统意义上的数据库不同，它需要接纳各种独立，异构的数据，因此它需要通过ETL（抽取、清洗、转换）功能，将这些数据统一处理并汇总到数据仓库中，而将全部的数据汇总的好处就是数仓中包含了企业所有数据，解决了企业数据孤岛问题，在后期可以为企业提供统一的数据视图。因此，数据入仓前的ETL是数仓建设中尤为关键且有非常复杂的一件事。

稳定性
传统数据库更多的偏向于更新操作(CRUD)，而数据仓库则是更多的提供一种可靠的，长久数据的查询和分析能力。在生产场景种，数据一旦写入到数据仓库，大概率会被长期保存且基本不进行修改操作，除非企业针对特定数据设置数据生命周期。因此基于这种更新频率几乎为零的设计再加上数仓的分布式存储与高可用的搭建，保证了数仓的稳定性和完整性。

及时性
数仓不仅仅要存储了管理历史数据，同时还要能够实时接收新的集成数据，通过这种快速反应历史数据与新增数据差异对比的能力，能够快速给决策和分析人员提供参考依据，这也是数仓建设的最终目的。
""")
    ui.show()
    sys.exit(app.exec())
