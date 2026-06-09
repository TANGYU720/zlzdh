<template>
  <div class="news">
    <section class="page-header">
      <div class="container">
        <h1>行业资讯</h1>
        <p>了解自动化行业最新动态和技术趋势</p>
      </div>
    </section>

    <section class="news-content">
      <div class="container">
        <div class="news-sidebar">
          <div class="sidebar-section">
            <h3>资讯分类</h3>
            <ul>
              <li :class="{ active: activeCategory === 'all' }" @click="activeCategory = 'all'">全部资讯</li>
              <li :class="{ active: activeCategory === 'technology' }" @click="activeCategory = 'technology'">技术动态</li>
              <li :class="{ active: activeCategory === 'market' }" @click="activeCategory = 'market'">市场分析</li>
              <li :class="{ active: activeCategory === 'policy' }" @click="activeCategory = 'policy'">政策法规</li>
              <li :class="{ active: activeCategory === 'case' }" @click="activeCategory = 'case'">案例分享</li>
            </ul>
          </div>
          <div class="sidebar-section">
            <h3>热门标签</h3>
            <div class="tags">
              <span class="tag">工业4.0</span>
              <span class="tag">智能制造</span>
              <span class="tag">AI</span>
              <span class="tag">物联网</span>
              <span class="tag">机器人</span>
              <span class="tag">大数据</span>
            </div>
          </div>
        </div>

        <div class="news-main">
          <div class="news-filters">
            <select v-model="sortBy">
              <option value="newest">最新发布</option>
              <option value="popular">最受欢迎</option>
            </select>
          </div>

          <div class="news-list">
            <div class="news-item" v-for="news in filteredNews" :key="news.id">
              <div class="news-image">📰</div>
              <div class="news-info">
                <div class="news-meta">
                  <span class="news-category">{{ getCategoryName(news.category) }}</span>
                  <span class="news-date">{{ news.date }}</span>
                </div>
                <h3>{{ news.title }}</h3>
                <p>{{ news.summary }}</p>
                <button class="read-more">阅读全文 →</button>
              </div>
            </div>
          </div>

          <div class="pagination">
            <button class="page-btn" :disabled="currentPage === 1">上一页</button>
            <span class="page-info">第 {{ currentPage }} / {{ totalPages }} 页</span>
            <button class="page-btn" :disabled="currentPage === totalPages">下一页</button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const activeCategory = ref('all')
const sortBy = ref('newest')
const currentPage = ref(1)

const newsList = ref([
  {
    id: 1,
    title: '工业4.0技术助力制造业转型升级',
    summary: '新一代工业自动化技术正在深刻改变传统制造业的生产模式，智能制造、物联网、大数据等技术的应用，使得生产效率大幅提升，生产成本显著降低。',
    date: '2026-06-09',
    category: 'technology'
  },
  {
    id: 2,
    title: '人工智能在智能制造中的应用',
    summary: 'AI技术与工业自动化的深度融合，开启智能工厂新纪元。机器学习算法能够预测设备故障，实现预防性维护，大幅降低停机时间。',
    date: '2026-06-08',
    category: 'technology'
  },
  {
    id: 3,
    title: '5G技术推动工业互联网发展',
    summary: '5G网络为工业设备互联互通提供了高速可靠的通信保障，实时数据传输、远程控制等应用场景正在成为现实。',
    date: '2026-06-07',
    category: 'technology'
  },
  {
    id: 4,
    title: '2026年自动化市场趋势分析',
    summary: '根据最新市场研究报告，全球工业自动化市场预计在未来五年内保持年均8%的增长率，亚太地区将成为主要增长引擎。',
    date: '2026-06-06',
    category: 'market'
  },
  {
    id: 5,
    title: '工业机器人市场持续增长',
    summary: '随着劳动力成本上升和技术进步，工业机器人的应用范围不断扩大，从传统制造业向物流、医疗等领域延伸。',
    date: '2026-06-05',
    category: 'market'
  },
  {
    id: 6,
    title: '新政策助力制造业高质量发展',
    summary: '国家出台一系列政策支持制造业转型升级，鼓励企业采用先进自动化技术，推动产业向高端化、智能化、绿色化方向发展。',
    date: '2026-06-04',
    category: 'policy'
  },
  {
    id: 7,
    title: '某汽车制造厂智能改造案例',
    summary: '通过引入自动化生产线和MES系统，该汽车制造厂实现了生产效率提升30%，产品合格率提升至99.5%。',
    date: '2026-06-03',
    category: 'case'
  },
  {
    id: 8,
    title: '数字化转型成功案例分享',
    summary: '一家传统机械制造企业通过三年的数字化转型，实现了从设计到生产的全流程数字化管理，企业竞争力显著提升。',
    date: '2026-06-02',
    category: 'case'
  }
])

const filteredNews = computed(() => {
  let result = newsList.value
  if (activeCategory.value !== 'all') {
    result = result.filter(n => n.category === activeCategory.value)
  }
  if (sortBy.value === 'newest') {
    result = [...result].sort((a, b) => new Date(b.date) - new Date(a.date))
  }
  return result
})

const totalPages = computed(() => Math.ceil(filteredNews.value.length / 4))

const getCategoryName = (category) => {
  const names = {
    technology: '技术动态',
    market: '市场分析',
    policy: '政策法规',
    case: '案例分享'
  }
  return names[category] || '其他'
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

.news-content {
  padding: 40px 0;
}

.news-content .container {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 2rem;
}

.news-sidebar {
  position: sticky;
  top: 100px;
  height: fit-content;
}

.sidebar-section {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.sidebar-section h3 {
  margin-bottom: 1rem;
  color: #0f172a;
}

.sidebar-section ul {
  list-style: none;
}

.sidebar-section ul li {
  padding: 0.5rem 0;
  cursor: pointer;
  color: #64748b;
  transition: color 0.3s;
}

.sidebar-section ul li:hover,
.sidebar-section ul li.active {
  color: #06b6d4;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  background: #f1f5f9;
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  font-size: 0.85rem;
  color: #64748b;
  cursor: pointer;
  transition: all 0.3s;
}

.tag:hover {
  background: #06b6d4;
  color: white;
}

.news-main {
  background: white;
  border-radius: 8px;
  padding: 2rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.news-filters {
  margin-bottom: 2rem;
}

.news-filters select {
  padding: 0.5rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  background: white;
  cursor: pointer;
}

.news-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.news-item {
  display: flex;
  gap: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e2e8f0;
}

.news-item:last-child {
  border-bottom: none;
}

.news-image {
  font-size: 3rem;
  flex-shrink: 0;
}

.news-info {
  flex: 1;
}

.news-meta {
  display: flex;
  gap: 1rem;
  margin-bottom: 0.5rem;
}

.news-category {
  background: #06b6d4;
  color: white;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  font-size: 0.8rem;
}

.news-date {
  color: #94a3b8;
  font-size: 0.9rem;
}

.news-info h3 {
  color: #0f172a;
  margin-bottom: 0.5rem;
  font-size: 1.2rem;
}

.news-info p {
  color: #64748b;
  margin-bottom: 1rem;
}

.read-more {
  background: transparent;
  border: none;
  color: #06b6d4;
  font-weight: 500;
  cursor: pointer;
  transition: color 0.3s;
}

.read-more:hover {
  color: #0891b2;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin-top: 2rem;
}

.page-btn {
  padding: 0.5rem 1rem;
  background: #f1f5f9;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s;
}

.page-btn:hover:not(:disabled) {
  background: #06b6d4;
  color: white;
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-info {
  color: #64748b;
}

@media (max-width: 768px) {
  .news-content .container {
    grid-template-columns: 1fr;
  }
  
  .news-item {
    flex-direction: column;
  }
}
</style>
