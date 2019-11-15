# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class Conditions(AbstractModel):
    """状态

    """

    def __init__(self):
        """
        :param Reason: 原因
        :type Reason: str
        :param Count: 具有相同原因的副本个数
        :type Count: int
        """
        self.Reason = None
        self.Count = None


    def _deserialize(self, params):
        self.Reason = params.get("Reason")
        self.Count = params.get("Count")


class Config(AbstractModel):
    """配置

    """

    def __init__(self):
        """
        :param Id: Id
        :type Id: str
        :param Name: 配置名
        :type Name: str
        :param ModelUri: 模型地址
        :type ModelUri: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Runtime: 运行环境
        :type Runtime: str
        :param Version: 配置版本
        :type Version: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Description: 配置描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self.Id = None
        self.Name = None
        self.ModelUri = None
        self.CreateTime = None
        self.Runtime = None
        self.Version = None
        self.UpdateTime = None
        self.Description = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.ModelUri = params.get("ModelUri")
        self.CreateTime = params.get("CreateTime")
        self.Runtime = params.get("Runtime")
        self.Version = params.get("Version")
        self.UpdateTime = params.get("UpdateTime")
        self.Description = params.get("Description")


class CreateJobRequest(AbstractModel):
    """CreateJob请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 任务名称
        :type Name: str
        :param WorkerCount: 同时处理任务的 Worker 个数
        :type WorkerCount: int
        :param ConfigId: 使用的配置 Id
        :type ConfigId: str
        :param Cpu: 处理器配置, 单位为1/1000核；范围[100, 256000]
        :type Cpu: int
        :param Memory: 内存配置, 单位为1M；范围[100, 256000]
        :type Memory: int
        :param Cluster: 运行集群
        :type Cluster: str
        :param PredictInput: 预测输入
        :type PredictInput: :class:`tencentcloud.tiems.v20190416.models.PredictInput`
        :param Description: 任务描述
        :type Description: str
        :param ResourceGroupId: 使用的资源组 Id，默认使用共享资源组
        :type ResourceGroupId: str
        :param Gpu: GPU算力配置，单位为1/1000 卡，范围 [0, 256000]
        :type Gpu: int
        :param GpuMemory: 显存配置, 单位为1M，范围 [0, 256000]
        :type GpuMemory: int
        :param GpuType: GPU类型
        :type GpuType: str
        """
        self.Name = None
        self.WorkerCount = None
        self.ConfigId = None
        self.Cpu = None
        self.Memory = None
        self.Cluster = None
        self.PredictInput = None
        self.Description = None
        self.ResourceGroupId = None
        self.Gpu = None
        self.GpuMemory = None
        self.GpuType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.WorkerCount = params.get("WorkerCount")
        self.ConfigId = params.get("ConfigId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Cluster = params.get("Cluster")
        if params.get("PredictInput") is not None:
            self.PredictInput = PredictInput()
            self.PredictInput._deserialize(params.get("PredictInput"))
        self.Description = params.get("Description")
        self.ResourceGroupId = params.get("ResourceGroupId")
        self.Gpu = params.get("Gpu")
        self.GpuMemory = params.get("GpuMemory")
        self.GpuType = params.get("GpuType")


class CreateJobResponse(AbstractModel):
    """CreateJob返回参数结构体

    """

    def __init__(self):
        """
        :param Job: 任务
        :type Job: :class:`tencentcloud.tiems.v20190416.models.Job`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Job = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        self.RequestId = params.get("RequestId")


class CreateRuntimeRequest(AbstractModel):
    """CreateRuntime请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 全局唯一的运行环境名称
        :type Name: str
        :param Image: 运行环境镜像地址
        :type Image: str
        :param Framework: 运行环境框架
        :type Framework: str
        :param Description: 运行环境描述
        :type Description: str
        :param HealthCheckOn: 是否支持健康检查，默认为False
        :type HealthCheckOn: bool
        """
        self.Name = None
        self.Image = None
        self.Framework = None
        self.Description = None
        self.HealthCheckOn = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Image = params.get("Image")
        self.Framework = params.get("Framework")
        self.Description = params.get("Description")
        self.HealthCheckOn = params.get("HealthCheckOn")


class CreateRuntimeResponse(AbstractModel):
    """CreateRuntime返回参数结构体

    """

    def __init__(self):
        """
        :param Runtime: 运行环境
        :type Runtime: :class:`tencentcloud.tiems.v20190416.models.Runtime`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Runtime = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Runtime") is not None:
            self.Runtime = Runtime()
            self.Runtime._deserialize(params.get("Runtime"))
        self.RequestId = params.get("RequestId")


class CreateServiceConfigRequest(AbstractModel):
    """CreateServiceConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 配置名称
        :type Name: str
        :param Runtime: 运行环境
        :type Runtime: str
        :param ModelUri: 模型地址，支持cos路径，格式为 cos://bucket名-appid.cos.region名.myqcloud.com/模型文件夹路径。为模型文件的上一层文件夹地址。
        :type ModelUri: str
        :param Description: 配置描述
        :type Description: str
        """
        self.Name = None
        self.Runtime = None
        self.ModelUri = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Runtime = params.get("Runtime")
        self.ModelUri = params.get("ModelUri")
        self.Description = params.get("Description")


class CreateServiceConfigResponse(AbstractModel):
    """CreateServiceConfig返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceConfig: 服务配置
        :type ServiceConfig: :class:`tencentcloud.tiems.v20190416.models.Config`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceConfig") is not None:
            self.ServiceConfig = Config()
            self.ServiceConfig._deserialize(params.get("ServiceConfig"))
        self.RequestId = params.get("RequestId")


class CreateServiceRequest(AbstractModel):
    """CreateService请求参数结构体

    """

    def __init__(self):
        """
        :param Scaler: 扩缩容配置
        :type Scaler: :class:`tencentcloud.tiems.v20190416.models.Scaler`
        :param ServiceConfigId: 服务配置Id
        :type ServiceConfigId: str
        :param Name: 服务名称
        :type Name: str
        :param ScaleMode: 扩缩容方式，支持AUTO, MANUAL，分别表示自动扩缩容和手动扩缩容
        :type ScaleMode: str
        :param Cpu: 处理器配置, 单位为1/1000核；范围[100, 256000]
        :type Cpu: int
        :param Memory: 内存配置, 单位为1M；范围[100, 256000]
        :type Memory: int
        :param Cluster: 集群，不填则使用默认集群
        :type Cluster: str
        :param ResourceGroupId: 部署要使用的资源组Id，默认为共享资源组
        :type ResourceGroupId: str
        :param Authentication: 默认为空，表示不需要鉴权，TOKEN 表示选择 Token 鉴权方式
        :type Authentication: str
        :param Gpu: GPU算力配置，单位为1/1000 卡，范围 [0, 256000]
        :type Gpu: int
        :param GpuMemory: 显存配置, 单位为1M，范围 [0, 256000]
        :type GpuMemory: int
        :param Description: 备注
        :type Description: str
        :param GpuType: GPU类型
        :type GpuType: str
        """
        self.Scaler = None
        self.ServiceConfigId = None
        self.Name = None
        self.ScaleMode = None
        self.Cpu = None
        self.Memory = None
        self.Cluster = None
        self.ResourceGroupId = None
        self.Authentication = None
        self.Gpu = None
        self.GpuMemory = None
        self.Description = None
        self.GpuType = None


    def _deserialize(self, params):
        if params.get("Scaler") is not None:
            self.Scaler = Scaler()
            self.Scaler._deserialize(params.get("Scaler"))
        self.ServiceConfigId = params.get("ServiceConfigId")
        self.Name = params.get("Name")
        self.ScaleMode = params.get("ScaleMode")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Cluster = params.get("Cluster")
        self.ResourceGroupId = params.get("ResourceGroupId")
        self.Authentication = params.get("Authentication")
        self.Gpu = params.get("Gpu")
        self.GpuMemory = params.get("GpuMemory")
        self.Description = params.get("Description")
        self.GpuType = params.get("GpuType")


class CreateServiceResponse(AbstractModel):
    """CreateService返回参数结构体

    """

    def __init__(self):
        """
        :param Service: 服务
        :type Service: :class:`tencentcloud.tiems.v20190416.models.ModelService`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Service = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self.Service = ModelService()
            self.Service._deserialize(params.get("Service"))
        self.RequestId = params.get("RequestId")


class DeleteJobRequest(AbstractModel):
    """DeleteJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 任务 Id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DeleteJobResponse(AbstractModel):
    """DeleteJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuntimeRequest(AbstractModel):
    """DeleteRuntime请求参数结构体

    """

    def __init__(self):
        """
        :param Runtime: 要删除的Runtime名
        :type Runtime: str
        """
        self.Runtime = None


    def _deserialize(self, params):
        self.Runtime = params.get("Runtime")


class DeleteRuntimeResponse(AbstractModel):
    """DeleteRuntime返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceConfigRequest(AbstractModel):
    """DeleteServiceConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceConfigId: 服务配置Id
        :type ServiceConfigId: str
        :param ServiceConfigName: 服务配置名称
        :type ServiceConfigName: str
        """
        self.ServiceConfigId = None
        self.ServiceConfigName = None


    def _deserialize(self, params):
        self.ServiceConfigId = params.get("ServiceConfigId")
        self.ServiceConfigName = params.get("ServiceConfigName")


class DeleteServiceConfigResponse(AbstractModel):
    """DeleteServiceConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceRequest(AbstractModel):
    """DeleteService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务Id
        :type ServiceId: str
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")


class DeleteServiceResponse(AbstractModel):
    """DeleteService返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 筛选选项
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为200
        :type Limit: int
        :param Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param OrderField: 排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        :param ResourceGroupId: 要查询的资源组 ID
        :type ResourceGroupId: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None
        self.ResourceGroupId = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        self.ResourceGroupId = params.get("ResourceGroupId")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 资源组下节点总数
        :type TotalCount: int
        :param Instances: 资源组下节点列表
        :type Instances: list of Instance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRuntimesRequest(AbstractModel):
    """DescribeRuntimes请求参数结构体

    """


class DescribeRuntimesResponse(AbstractModel):
    """DescribeRuntimes返回参数结构体

    """

    def __init__(self):
        """
        :param Runtimes: TIEMS支持的运行环境列表
        :type Runtimes: list of Runtime
        :param UserAccess: 用户对runtime对权限
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAccess: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Runtimes = None
        self.UserAccess = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Runtimes") is not None:
            self.Runtimes = []
            for item in params.get("Runtimes"):
                obj = Runtime()
                obj._deserialize(item)
                self.Runtimes.append(obj)
        self.UserAccess = params.get("UserAccess")
        self.RequestId = params.get("RequestId")


class DescribeServiceConfigsRequest(AbstractModel):
    """DescribeServiceConfigs请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 筛选选项，支持按照name等进行筛选
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为1000
        :type Limit: int
        :param Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param OrderField: 排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        :param PageByName: 是否按照配置名分页
        :type PageByName: bool
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None
        self.PageByName = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        self.PageByName = params.get("PageByName")


class DescribeServiceConfigsResponse(AbstractModel):
    """DescribeServiceConfigs返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceConfigs: 服务配置
        :type ServiceConfigs: list of Config
        :param TotalCount: 服务配置总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceConfigs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceConfigs") is not None:
            self.ServiceConfigs = []
            for item in params.get("ServiceConfigs"):
                obj = Config()
                obj._deserialize(item)
                self.ServiceConfigs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeServicesRequest(AbstractModel):
    """DescribeServices请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 筛选选项，支持按照name等字段进行筛选
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param OrderField: 排序的依据字段， 取值范围 "CREATE_TIME" "UPDATE_TIME"
        :type OrderField: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")


class DescribeServicesResponse(AbstractModel):
    """DescribeServices返回参数结构体

    """

    def __init__(self):
        """
        :param Services: 服务列表
        :type Services: list of ModelService
        :param TotalCount: 服务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Services = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Services") is not None:
            self.Services = []
            for item in params.get("Services"):
                obj = ModelService()
                obj._deserialize(item)
                self.Services.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class Expose(AbstractModel):
    """服务暴露方式

    """

    def __init__(self):
        """
        :param ExposeType: 暴露方式，支持 EXTERNAL（外网暴露），VPC （VPC内网打通）
        :type ExposeType: str
        :param Ip: 暴露Ip。暴露方式为 EXTERNAL 为外网 Ip，暴露方式为 VPC 时为指定 Vpc 下的Vip
        :type Ip: str
        :param UnVpcId: 暴露方式为 VPC 时，打通的私有网络Id
注意：此字段可能返回 null，表示取不到有效值。
        :type UnVpcId: str
        :param UnSubnetId: 暴露方式为 VPC 时，打通的子网Id
注意：此字段可能返回 null，表示取不到有效值。
        :type UnSubnetId: str
        """
        self.ExposeType = None
        self.Ip = None
        self.UnVpcId = None
        self.UnSubnetId = None


    def _deserialize(self, params):
        self.ExposeType = params.get("ExposeType")
        self.Ip = params.get("Ip")
        self.UnVpcId = params.get("UnVpcId")
        self.UnSubnetId = params.get("UnSubnetId")


class Filter(AbstractModel):
    """筛选项

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Values: 取值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Instance(AbstractModel):
    """节点

    """

    def __init__(self):
        """
        :param Id: 节点 ID
        :type Id: str
        :param Zone: 节点所在地区
        :type Zone: str
        :param InstanceType: 节点类型
        :type InstanceType: str
        :param InstanceChargeType: 节点充值类型
        :type InstanceChargeType: str
        :param Cpu: Cpu 核数
        :type Cpu: int
        :param Memory: 内存
        :type Memory: int
        :param Gpu: Gpu 核数
        :type Gpu: int
        :param State: 节点状态
        :type State: str
        :param AbnormalReason: 节点故障信息
        :type AbnormalReason: str
        :param Created: 创建时间
        :type Created: str
        :param Updated: 更新时间
        :type Updated: str
        :param DeadlineTime: 到期时间
        :type DeadlineTime: str
        :param ResourceGroupId: 所属资源组 ID
        :type ResourceGroupId: str
        :param RenewFlag: 自动续费标签
        :type RenewFlag: str
        :param Region: 节点所在地域
        :type Region: str
        :param CpuRequested: 当前 Cpu 申请使用量
        :type CpuRequested: int
        :param MemoryRequested: 当前 Memory 申请使用量
        :type MemoryRequested: int
        :param GpuRequested: 当前 Gpu 申请使用量
        :type GpuRequested: int
        """
        self.Id = None
        self.Zone = None
        self.InstanceType = None
        self.InstanceChargeType = None
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.State = None
        self.AbnormalReason = None
        self.Created = None
        self.Updated = None
        self.DeadlineTime = None
        self.ResourceGroupId = None
        self.RenewFlag = None
        self.Region = None
        self.CpuRequested = None
        self.MemoryRequested = None
        self.GpuRequested = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Gpu = params.get("Gpu")
        self.State = params.get("State")
        self.AbnormalReason = params.get("AbnormalReason")
        self.Created = params.get("Created")
        self.Updated = params.get("Updated")
        self.DeadlineTime = params.get("DeadlineTime")
        self.ResourceGroupId = params.get("ResourceGroupId")
        self.RenewFlag = params.get("RenewFlag")
        self.Region = params.get("Region")
        self.CpuRequested = params.get("CpuRequested")
        self.MemoryRequested = params.get("MemoryRequested")
        self.GpuRequested = params.get("GpuRequested")


class Job(AbstractModel):
    """任务

    """

    def __init__(self):
        """
        :param Id: 任务 Id
        :type Id: str
        :param Cluster: 集群名
        :type Cluster: str
        :param Region: Region 名
        :type Region: str
        :param Name: 任务名称
        :type Name: str
        :param Runtime: Worker 使用的运行环境
        :type Runtime: str
        :param Description: 任务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param ConfigId: 配置 Id
        :type ConfigId: str
        :param PredictInput: 预测输入
        :type PredictInput: :class:`tencentcloud.tiems.v20190416.models.PredictInput`
        :param Status: 任务状态
        :type Status: :class:`tencentcloud.tiems.v20190416.models.JobStatus`
        :param CreateTime: 任务创建时间
        :type CreateTime: str
        :param StartTime: 任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param CancelTime: 任务取消时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CancelTime: str
        :param ResourceGroupId: 任务使用资源组 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param Cpu: 处理器配置, 单位为1/1000核；范围[100, 256000]
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param Memory: 内存配置, 单位为1M；范围[100, 256000]
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param Gpu: GPU算力配置，单位为1/1000 卡，范围 [0, 256000]
注意：此字段可能返回 null，表示取不到有效值。
        :type Gpu: int
        :param GpuMemory: 显存配置, 单位为1M，范围 [0, 256000]
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuMemory: int
        :param ResourceGroupName: 任务使用资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param GpuType: GPU类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuType: str
        :param ConfigName: 配置名
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigName: str
        :param ConfigVersion: 配置版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigVersion: str
        """
        self.Id = None
        self.Cluster = None
        self.Region = None
        self.Name = None
        self.Runtime = None
        self.Description = None
        self.ConfigId = None
        self.PredictInput = None
        self.Status = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.CancelTime = None
        self.ResourceGroupId = None
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.GpuMemory = None
        self.ResourceGroupName = None
        self.GpuType = None
        self.ConfigName = None
        self.ConfigVersion = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Cluster = params.get("Cluster")
        self.Region = params.get("Region")
        self.Name = params.get("Name")
        self.Runtime = params.get("Runtime")
        self.Description = params.get("Description")
        self.ConfigId = params.get("ConfigId")
        if params.get("PredictInput") is not None:
            self.PredictInput = PredictInput()
            self.PredictInput._deserialize(params.get("PredictInput"))
        if params.get("Status") is not None:
            self.Status = JobStatus()
            self.Status._deserialize(params.get("Status"))
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CancelTime = params.get("CancelTime")
        self.ResourceGroupId = params.get("ResourceGroupId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Gpu = params.get("Gpu")
        self.GpuMemory = params.get("GpuMemory")
        self.ResourceGroupName = params.get("ResourceGroupName")
        self.GpuType = params.get("GpuType")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")


class JobStatus(AbstractModel):
    """任务状态

    """

    def __init__(self):
        """
        :param Status: 任务状态
        :type Status: str
        :param Message: 错误时为错误描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param DesiredWorkers: 预期Worker数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredWorkers: int
        :param CurrentWorkers: 当前Worker数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentWorkers: int
        :param Replicas: 副本名
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: list of str
        """
        self.Status = None
        self.Message = None
        self.DesiredWorkers = None
        self.CurrentWorkers = None
        self.Replicas = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.DesiredWorkers = params.get("DesiredWorkers")
        self.CurrentWorkers = params.get("CurrentWorkers")
        self.Replicas = params.get("Replicas")


class ModelService(AbstractModel):
    """模型服务

    """

    def __init__(self):
        """
        :param Id: 服务ID
        :type Id: str
        :param Cluster: 运行集群
注意：此字段可能返回 null，表示取不到有效值。
        :type Cluster: str
        :param Name: 服务名称
        :type Name: str
        :param Runtime: 运行环境
        :type Runtime: str
        :param ModelUri: 模型地址
        :type ModelUri: str
        :param Cpu: 处理器配置, 单位为1/1000核
        :type Cpu: int
        :param Memory: 内存配置, 单位为1M
        :type Memory: int
        :param Gpu: GPU 配置, 单位为1/1000 卡
        :type Gpu: int
        :param GpuMemory: 显存配置, 单位为1M
        :type GpuMemory: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param ScaleMode: 支持AUTO, MANUAL
        :type ScaleMode: str
        :param Scaler: 弹性伸缩配置
        :type Scaler: :class:`tencentcloud.tiems.v20190416.models.Scaler`
        :param Status: 服务状态
        :type Status: :class:`tencentcloud.tiems.v20190416.models.ServiceStatus`
        :param AccessToken: 访问密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessToken: str
        :param ConfigId: 服务配置Id
        :type ConfigId: str
        :param ConfigName: 服务配置名
        :type ConfigName: str
        :param ServeSeconds: 服务运行时长
        :type ServeSeconds: int
        :param ConfigVersion: 配置版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigVersion: str
        :param ResourceGroupId: 服务使用资源组 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param Exposes: 暴露方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Exposes: list of Expose
        :param Region: Region 名
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param ResourceGroupName: 服务使用资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param Description: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param GpuType: GPU类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuType: str
        """
        self.Id = None
        self.Cluster = None
        self.Name = None
        self.Runtime = None
        self.ModelUri = None
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.GpuMemory = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ScaleMode = None
        self.Scaler = None
        self.Status = None
        self.AccessToken = None
        self.ConfigId = None
        self.ConfigName = None
        self.ServeSeconds = None
        self.ConfigVersion = None
        self.ResourceGroupId = None
        self.Exposes = None
        self.Region = None
        self.ResourceGroupName = None
        self.Description = None
        self.GpuType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Cluster = params.get("Cluster")
        self.Name = params.get("Name")
        self.Runtime = params.get("Runtime")
        self.ModelUri = params.get("ModelUri")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Gpu = params.get("Gpu")
        self.GpuMemory = params.get("GpuMemory")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ScaleMode = params.get("ScaleMode")
        if params.get("Scaler") is not None:
            self.Scaler = Scaler()
            self.Scaler._deserialize(params.get("Scaler"))
        if params.get("Status") is not None:
            self.Status = ServiceStatus()
            self.Status._deserialize(params.get("Status"))
        self.AccessToken = params.get("AccessToken")
        self.ConfigId = params.get("ConfigId")
        self.ConfigName = params.get("ConfigName")
        self.ServeSeconds = params.get("ServeSeconds")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ResourceGroupId = params.get("ResourceGroupId")
        if params.get("Exposes") is not None:
            self.Exposes = []
            for item in params.get("Exposes"):
                obj = Expose()
                obj._deserialize(item)
                self.Exposes.append(obj)
        self.Region = params.get("Region")
        self.ResourceGroupName = params.get("ResourceGroupName")
        self.Description = params.get("Description")
        self.GpuType = params.get("GpuType")


class Option(AbstractModel):
    """配置项

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Value: 取值
        :type Value: int
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class PredictInput(AbstractModel):
    """预测输入

    """

    def __init__(self):
        """
        :param InputPath: 输入路径，支持 cos 格式路径文件夹或文件
        :type InputPath: str
        :param OutputPath: 输出路径，支持 cos 格式路径
        :type OutputPath: str
        :param InputDataFormat: 输入数据格式，目前支持：JSON
        :type InputDataFormat: str
        :param OutputDataFormat: 输出数据格式，目前支持：JSON
        :type OutputDataFormat: str
        :param BatchSize: 预测批大小，默认为 64
        :type BatchSize: int
        :param SignatureName: 模型签名
注意：此字段可能返回 null，表示取不到有效值。
        :type SignatureName: str
        """
        self.InputPath = None
        self.OutputPath = None
        self.InputDataFormat = None
        self.OutputDataFormat = None
        self.BatchSize = None
        self.SignatureName = None


    def _deserialize(self, params):
        self.InputPath = params.get("InputPath")
        self.OutputPath = params.get("OutputPath")
        self.InputDataFormat = params.get("InputDataFormat")
        self.OutputDataFormat = params.get("OutputDataFormat")
        self.BatchSize = params.get("BatchSize")
        self.SignatureName = params.get("SignatureName")


class Runtime(AbstractModel):
    """运行环境

    """

    def __init__(self):
        """
        :param Name: 运行环境名称
        :type Name: str
        :param Framework: 运行环境框架
        :type Framework: str
        :param Description: 运行环境描述
        :type Description: str
        :param Public: 是否为公开运行环境
注意：此字段可能返回 null，表示取不到有效值。
        :type Public: bool
        :param HealthCheckOn: 是否打开健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckOn: bool
        :param Image: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.Name = None
        self.Framework = None
        self.Description = None
        self.Public = None
        self.HealthCheckOn = None
        self.Image = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Framework = params.get("Framework")
        self.Description = params.get("Description")
        self.Public = params.get("Public")
        self.HealthCheckOn = params.get("HealthCheckOn")
        self.Image = params.get("Image")
        self.CreateTime = params.get("CreateTime")


class Scaler(AbstractModel):
    """扩缩容配置

    """

    def __init__(self):
        """
        :param MaxReplicas: 最大副本数
        :type MaxReplicas: int
        :param MinReplicas: 最小副本数
        :type MinReplicas: int
        :param StartReplicas: 起始副本数
        :type StartReplicas: int
        :param HpaMetrics: 扩缩容指标，选择自动扩缩容时至少需要选择一个指标，支持CPU-UTIL、MEMORY-UTIL
        :type HpaMetrics: list of Option
        """
        self.MaxReplicas = None
        self.MinReplicas = None
        self.StartReplicas = None
        self.HpaMetrics = None


    def _deserialize(self, params):
        self.MaxReplicas = params.get("MaxReplicas")
        self.MinReplicas = params.get("MinReplicas")
        self.StartReplicas = params.get("StartReplicas")
        if params.get("HpaMetrics") is not None:
            self.HpaMetrics = []
            for item in params.get("HpaMetrics"):
                obj = Option()
                obj._deserialize(item)
                self.HpaMetrics.append(obj)


class ServiceStatus(AbstractModel):
    """服务状态

    """

    def __init__(self):
        """
        :param DesiredReplicas: 预期副本数
        :type DesiredReplicas: int
        :param CurrentReplicas: 当前副本数
        :type CurrentReplicas: int
        :param Status: Normal：正常运行中；Abnormal：服务异常，例如容器启动失败等；Waiting：服务等待中，例如容器下载镜像过程等；Stopped：已停止 Stopping 停止中；Resuming：重启中；Updating：服务更新中
        :type Status: str
        :param Conditions: 服务处于当前状态的原因集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of Conditions
        :param Replicas: 副本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: list of str
        :param Message: 运行状态对额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.DesiredReplicas = None
        self.CurrentReplicas = None
        self.Status = None
        self.Conditions = None
        self.Replicas = None
        self.Message = None


    def _deserialize(self, params):
        self.DesiredReplicas = params.get("DesiredReplicas")
        self.CurrentReplicas = params.get("CurrentReplicas")
        self.Status = params.get("Status")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = Conditions()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.Replicas = params.get("Replicas")
        self.Message = params.get("Message")


class UpdateJobRequest(AbstractModel):
    """UpdateJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 任务 Id
        :type JobId: str
        :param JobAction: 任务更新动作，支持：Cancel
        :type JobAction: str
        :param Description: 备注
        :type Description: str
        """
        self.JobId = None
        self.JobAction = None
        self.Description = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobAction = params.get("JobAction")
        self.Description = params.get("Description")


class UpdateJobResponse(AbstractModel):
    """UpdateJob返回参数结构体

    """

    def __init__(self):
        """
        :param Job: 任务
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: :class:`tencentcloud.tiems.v20190416.models.Job`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Job = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        self.RequestId = params.get("RequestId")


class UpdateServiceRequest(AbstractModel):
    """UpdateService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务Id
        :type ServiceId: str
        :param Scaler: 扩缩容配置
        :type Scaler: :class:`tencentcloud.tiems.v20190416.models.Scaler`
        :param ServiceConfigId: 服务配置Id
        :type ServiceConfigId: str
        :param ScaleMode: 支持AUTO, MANUAL，分别表示自动扩缩容，手动扩缩容
        :type ScaleMode: str
        :param ServiceAction: 支持STOP(停止) RESUME(重启)
        :type ServiceAction: str
        :param Description: 备注
        :type Description: str
        :param GpuType: GPU卡类型
        :type GpuType: str
        """
        self.ServiceId = None
        self.Scaler = None
        self.ServiceConfigId = None
        self.ScaleMode = None
        self.ServiceAction = None
        self.Description = None
        self.GpuType = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        if params.get("Scaler") is not None:
            self.Scaler = Scaler()
            self.Scaler._deserialize(params.get("Scaler"))
        self.ServiceConfigId = params.get("ServiceConfigId")
        self.ScaleMode = params.get("ScaleMode")
        self.ServiceAction = params.get("ServiceAction")
        self.Description = params.get("Description")
        self.GpuType = params.get("GpuType")


class UpdateServiceResponse(AbstractModel):
    """UpdateService返回参数结构体

    """

    def __init__(self):
        """
        :param Service: 服务
        :type Service: :class:`tencentcloud.tiems.v20190416.models.ModelService`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Service = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self.Service = ModelService()
            self.Service._deserialize(params.get("Service"))
        self.RequestId = params.get("RequestId")