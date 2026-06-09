<template>
  <div class="downloads">
    <section class="page-header">
      <div class="container">
        <h1>资源下载</h1>
        <p>下载自动化行业相关的技术文档、软件工具和资料</p>
      </div>
    </section>

    <section class="downloads-content">
      <div class="container">
        <div class="download-categories">
          <div 
            class="category-card" 
            v-for="category in categories" 
            :key="category.id"
            :class="{ active: activeCategory === category.id }"
            @click="activeCategory = category.id"
          >
            <div class="category-icon">{{ category.icon }}</div>
            <div class="category-info">
              <h3>{{ category.name }}</h3>
              <p>{{ category.count }} 个资源</p>
            </div>
          </div>
        </div>

        <div class="download-list">
          <div class="download-header">
            <h2>{{ getCategoryName(activeCategory) }}</h2>
            <div class="search-box">
              <input type="text" v-model="searchQuery" placeholder="搜索资源..." />
              <span class="search-icon">🔍</span>
            </div>
          </div>

          <div class="resources-grid">
            <div class="resource-card" v-for="resource in filteredResources" :key="resource.id">
              <div class="resource-icon">{{ resource.icon }}</div>
              <div class="resource-info">
                <h3>{{ resource.name }}</h3>
                <p>{{ resource.description }}</p>
                <div class="resource-meta">
                  <span class="file-type">{{ resource.type }}</span>
                  <span class="file-size">{{ resource.size }}</span>
                  <span class="download-count">⬇️ {{ resource.downloads }} 次下载</span>
                </div>
              </div>
              <button class="download-btn">
                <span>📥</span>
                <span>下载</span>
              </button>
            </div>
          </div>

          <div class="empty-state" v-if="filteredResources.length === 0">
            <span class="empty-icon">📭</span>
            <p>暂无相关资源</p>
          </div>
        </div>
      </div>
    </section>

    <section class="featured-resources">
      <div class="container">
        <h2>热门资源推荐</h2>
        <div class="featured-grid">
          <div class="featured-card" v-for="featured in featuredResources" :key="featured.id">
            <div class="featured-badge">🔥 热门</div>
            <div class="featured-icon">{{ featured.icon }}</div>
            <h3>{{ featured.name }}</h3>
            <p>{{ featured.description }}</p>
            <div class="featured-info">
              <span>{{ featured.type }}</span>
              <span>{{ featured.size }}</span>
            </div>
            <button class="download-btn primary">立即下载</button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const activeCategory = ref('datasheet')
const searchQuery = ref('')

const categories = ref([
  { id: 'datasheet', name: '产品手册', icon: '📋', count: 24 },
  { id: 'software', name: '软件工具', icon: '💻', count: 18 },
  { id: 'driver', name: '驱动程序', icon: '🔧', count: 35 },
  { id: 'manual', name: '技术手册', icon: '📖', count: 15 },
  { id: 'case', name: '案例资料', icon: '📊', count: 12 },
  { id: 'standard', name: '标准规范', icon: '📐', count: 8 }
])

const resources = ref([
  { id: 1, name: '西门子S7-1200产品手册', description: '西门子S7-1200系列PLC产品详细规格和技术参数', type: 'PDF', size: '2.5 MB', downloads: 1580, icon: '📄', category: 'datasheet' },
  { id: 2, name: '欧姆龙CP1H编程手册', description: '欧姆龙CP1H系列PLC编程指南和指令说明', type: 'PDF', size: '3.2 MB', downloads: 1250, icon: '📄', category: 'manual' },
  { id: 3, name: 'PLC编程软件V3.0', description: 'PLC编程调试软件，支持多种品牌PLC', type: 'EXE', size: '156 MB', downloads: 2300, icon: '💾', category: 'software' },
  { id: 4, name: '工业机器人技术白皮书', description: '工业机器人应用技术白皮书，包含选型指南', type: 'PDF', size: '1.8 MB', downloads: 980, icon: '📄', category: 'case' },
  { id: 5, name: '三菱FX系列驱动', description: '三菱FX系列PLC驱动程序安装包', type: 'ZIP', size: '12 MB', downloads: 1850, icon: '📦', category: 'driver' },
  { id: 6, name: '工业4.0标准规范', description: '工业4.0智能制造标准规范文档', type: 'PDF', size: '4.5 MB', downloads: 760, icon: '📄', category: 'standard' },
  { id: 7, name: 'SCADA系统设计指南', description: 'SCADA系统设计规范和最佳实践', type: 'PDF', size: '2.1 MB', downloads: 890, icon: '📄', category: 'manual' },
  { id: 8, name: '工业物联网网关软件', description: '工业物联网网关配置软件', type: 'EXE', size: '89 MB', downloads: 650, icon: '💾', category: 'software' },
  { id: 9, name: '施耐德PLC产品目录', description: '施耐德全系列PLC产品目录和选型手册', type: 'PDF', size: '5.2 MB', downloads: 1120, icon: '📄', category: 'datasheet' },
  { id: 10, name: '工业网络安全规范', description: '工业控制系统网络安全标准规范', type: 'PDF', size: '3.8 MB', downloads: 580, icon: '📄', category: 'standard' }
])

const featuredResources = ref([
  { id: 1, name: 'PLC编程入门教程', description: '从零开始学习PLC编程，包含大量实例和练习题', type: 'PDF', size: '12.5 MB', icon: '📚' },
  { id: 2, name: '工业自动化解决方案合集', description: '精选工业自动化解决方案案例集', type: 'PDF', size: '8.2 MB', icon: '📊' },
  { id: 3, name: 'MES系统实施指南', description: 'MES制造执行系统实施方法论和最佳实践', type: 'PDF', size: '6.8 MB', icon: '📖' }
])

const filteredResources = computed(() => {
  let result = resources.value.filter(r => r.category === activeCategory.value)
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(r => 
      r.name.toLowerCase().includes(query) || 
      r.description.toLowerCase().includes(query)
    )
  }
  return result
})

const getCategoryName = (categoryId) => {
  const category = categories.value.find(c => c.id === categoryId)
  return category ? category.name : '全部资源'
}
</script>

<style scoped>
.page-header {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  color: white;
  padding: 40px 0;
  text-align: center;
}

.page-header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.page-header p {
  color: #94a3b8;
}

.downloads-content {
  padding: 40px 0;
}

.download-categories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.category-card {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s;
  border: 2px solid transparent;
}

.category-card:hover,
.category-card.active {
  border-color: #06b6d4;
  background: #f0fdfa;
}

.category-icon {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.category-info h3 {
  color: #0f172a;
  font-size: 1rem;
  text-align: center;
}

.category-info p {
  color: #64748b;
  font-size: 0.85rem;
}

.download-list {
  background: white;
  border-radius: 8px;
  padding: 2rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.download-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.download-header h2 {
  color: #0f172a;
}

.search-box {
  position: relative;
}

.search-box input {
  padding: 0.5rem 2rem 0.5rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  width: 250px;
}

.search-icon {
  position: absolute;
  right: 0.5rem;
  top: 50%;
  transform: translateY(-50%);
}

.resources-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.resource-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: #f8fafc;
  border-radius: 8px;
  transition: all 0.3s;
}

.resource-card:hover {
  background: #f1f5f9;
}

.resource-icon {
  font-size: 2.5rem;
}

.resource-info {
  flex: 1;
}

.resource-info h3 {
  color: #0f172a;
  margin-bottom: 0.3rem;
}

.resource-info p {
  color: #64748b;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.resource-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.85rem;
  color: #94a3b8;
}

.file-type {
  background: #e0f2fe;
  color: #0284c7;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
}

.download-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 1.2rem;
  background: #f1f5f9;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s;
}

.download-btn:hover {
  background: #06b6d4;
  color: white;
  border-color: #06b6d4;
}

.download-btn.primary {
  background: linear-gradient(135deg, #06b6d4, #3b82f6);
  color: white;
  border: none;
}

.empty-state {
  text-align: center;
  padding: 3rem;
}

.empty-icon {
  font-size: 4rem;
  display: block;
  margin-bottom: 1rem;
}

.empty-state p {
  color: #64748b;
}

.featured-resources {
  padding: 40px 0;
  margin-top: 2rem;
}

.featured-resources h2 {
  text-align: center;
  color: #0f172a;
  margin-bottom: 2rem;
}

.featured-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.featured-card {
  background: linear-gradient(135deg, #0f172a, #1e293b);
  padding: 2rem;
  border-radius: 12px;
  color: white;
  position: relative;
}

.featured-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: #f59e0b;
  color: white;
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
  font-size: 0.8rem;
}

.featured-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.featured-card h3 {
  margin-bottom: 0.5rem;
}

.featured-card p {
  color: #94a3b8;
  margin-bottom: 1rem;
}

.featured-info {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
  color: #94a3b8;
}

@media (max-width: 768px) {
  .resource-card {
    flex-direction: column;
    text-align: center;
  }
  
  .resource-meta {
    justify-content: center;
  }
  
  .download-header {
    flex-direction: column;
  }
  
  .search-box input {
    width: 100%;
  }
}
</style>
