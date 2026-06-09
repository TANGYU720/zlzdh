<template>
  <div class="cases">
    <section class="page-header">
      <div class="container">
        <h1>项目案例</h1>
        <p>展示我们在自动化领域的成功案例</p>
      </div>
    </section>

    <section class="cases-content">
      <div class="container">
        <div class="case-filters">
          <button 
            v-for="filter in filters" 
            :key="filter.value"
            :class="{ active: activeFilter === filter.value }"
            @click="activeFilter = filter.value"
          >
            {{ filter.label }}
          </button>
        </div>

        <div class="cases-grid">
          <div class="case-card" v-for="caseItem in filteredCases" :key="caseItem.id">
            <div class="case-image">
              <span>{{ caseItem.icon }}</span>
            </div>
            <div class="case-info">
              <div class="case-category">{{ caseItem.category }}</div>
              <h3>{{ caseItem.title }}</h3>
              <p>{{ caseItem.summary }}</p>
              <div class="case-tags">
                <span v-for="tag in caseItem.tags" :key="tag" class="tag">{{ tag }}</span>
              </div>
              <div class="case-stats">
                <div class="stat">
                  <span class="stat-value">{{ caseItem.stats.efficiency }}</span>
                  <span class="stat-label">效率提升</span>
                </div>
                <div class="stat">
                  <span class="stat-value">{{ caseItem.stats.cost }}</span>
                  <span class="stat-label">成本降低</span>
                </div>
              </div>
              <button class="view-detail">查看详情 →</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="case-showcase">
      <div class="container">
        <div class="showcase-header">
          <h2>重点案例展示</h2>
          <p>深入了解我们的代表性项目</p>
        </div>
        <div class="showcase-content">
          <div class="showcase-image">🏭</div>
          <div class="showcase-info">
            <h3>某大型汽车制造厂智能生产线改造</h3>
            <p>为国内某知名汽车制造商提供完整的智能生产线解决方案，涵盖焊接、装配、检测等全流程自动化改造。</p>
            <ul class="showcase-features">
              <li>🤖 引入200+工业机器人</li>
              <li>📊 实时生产数据监控系统</li>
              <li>🔧 MES制造执行系统集成</li>
              <li>✅ 产品合格率提升至99.8%</li>
            </ul>
            <div class="showcase-stats">
              <div class="big-stat">
                <span class="value">30%</span>
                <span class="label">生产效率提升</span>
              </div>
              <div class="big-stat">
                <span class="value">40%</span>
                <span class="label">人工成本降低</span>
              </div>
              <div class="big-stat">
                <span class="value">50%</span>
                <span class="label">故障率降低</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const activeFilter = ref('all')

const filters = [
  { label: '全部', value: 'all' },
  { label: '汽车制造', value: 'automotive' },
  { label: '医药行业', value: 'pharmaceutical' },
  { label: '物流仓储', value: 'logistics' },
  { label: '电子制造', value: 'electronics' }
]

const cases = ref([
  {
    id: 1,
    title: '汽车零部件自动化生产线',
    summary: '为某汽车零部件企业设计并实施自动化装配线，实现关键零部件的全自动化生产。',
    category: '汽车制造',
    icon: '🚗',
    tags: ['自动化装配', '机器人焊接', '质量检测'],
    stats: { efficiency: '+25%', cost: '-18%' }
  },
  {
    id: 2,
    title: '医药洁净车间自动化',
    summary: '为制药企业提供符合GMP标准的洁净车间自动化解决方案，实现药品生产全程追溯。',
    category: '医药行业',
    icon: '💊',
    tags: ['洁净车间', 'GMP认证', '药品追溯'],
    stats: { efficiency: '+30%', cost: '-22%' }
  },
  {
    id: 3,
    title: '智能仓储物流系统',
    summary: '为电商物流中心打造智能仓储解决方案，包含AGV搬运机器人和自动化分拣系统。',
    category: '物流仓储',
    icon: '📦',
    tags: ['AGV机器人', '立体仓库', '自动分拣'],
    stats: { efficiency: '+40%', cost: '-25%' }
  },
  {
    id: 4,
    title: '电子元器件SMT生产线',
    summary: '为电子制造企业提供SMT生产线自动化改造，提升贴片精度和生产效率。',
    category: '电子制造',
    icon: '🔌',
    tags: ['SMT贴片', 'AOI检测', '智能焊接'],
    stats: { efficiency: '+35%', cost: '-20%' }
  },
  {
    id: 5,
    title: '新能源电池生产线',
    summary: '为新能源企业设计锂电池自动化生产线，实现电芯装配、检测、包装全流程自动化。',
    category: '电子制造',
    icon: '🔋',
    tags: ['电池装配', '性能检测', '自动化包装'],
    stats: { efficiency: '+28%', cost: '-15%' }
  },
  {
    id: 6,
    title: '食品包装自动化线',
    summary: '为食品加工企业提供自动化包装解决方案，包含称重、包装、贴标全流程自动化。',
    category: '医药行业',
    icon: '🍪',
    tags: ['自动称重', '真空包装', '智能贴标'],
    stats: { efficiency: '+32%', cost: '-18%' }
  }
])

const filteredCases = computed(() => {
  if (activeFilter.value === 'all') return cases.value
  const categoryMap = {
    automotive: '汽车制造',
    pharmaceutical: '医药行业',
    logistics: '物流仓储',
    electronics: '电子制造'
  }
  return cases.value.filter(c => c.category === categoryMap[activeFilter.value])
})
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

.cases-content {
  padding: 40px 0;
}

.case-filters {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.case-filters button {
  padding: 0.5rem 1.5rem;
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s;
}

.case-filters button:hover,
.case-filters button.active {
  background: #06b6d4;
  color: white;
  border-color: #06b6d4;
}

.cases-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
}

.case-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.case-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.case-image {
  background: linear-gradient(135deg, #0f172a, #1e293b);
  padding: 2rem;
  text-align: center;
}

.case-image span {
  font-size: 4rem;
}

.case-info {
  padding: 1.5rem;
}

.case-category {
  background: #06b6d4;
  color: white;
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
  font-size: 0.8rem;
  margin-bottom: 0.5rem;
  display: inline-block;
}

.case-info h3 {
  color: #0f172a;
  margin-bottom: 0.5rem;
}

.case-info p {
  color: #64748b;
  margin-bottom: 1rem;
}

.case-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.tag {
  background: #f1f5f9;
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
  font-size: 0.8rem;
  color: #64748b;
}

.case-stats {
  display: flex;
  gap: 2rem;
  margin-bottom: 1rem;
}

.stat {
  text-align: center;
}

.stat-value {
  display: block;
  font-size: 1.5rem;
  font-weight: bold;
  color: #06b6d4;
}

.stat-label {
  font-size: 0.8rem;
  color: #94a3b8;
}

.view-detail {
  width: 100%;
  padding: 0.8rem;
  background: linear-gradient(135deg, #06b6d4, #3b82f6);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.3s;
}

.view-detail:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(6, 182, 212, 0.3);
}

.case-showcase {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  padding: 60px 0;
  margin-top: 2rem;
}

.showcase-header {
  text-align: center;
  color: white;
  margin-bottom: 3rem;
}

.showcase-header h2 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.showcase-header p {
  color: #94a3b8;
}

.showcase-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.showcase-image {
  font-size: 12rem;
  text-align: center;
}

.showcase-info {
  color: white;
}

.showcase-info h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.showcase-info p {
  color: #94a3b8;
  margin-bottom: 1.5rem;
}

.showcase-features {
  list-style: none;
  margin-bottom: 2rem;
}

.showcase-features li {
  padding: 0.5rem 0;
  color: #cbd5e1;
}

.showcase-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.big-stat {
  text-align: center;
  padding: 1.5rem;
  background: rgba(6, 182, 212, 0.1);
  border-radius: 8px;
}

.big-stat .value {
  display: block;
  font-size: 2rem;
  font-weight: bold;
  color: #06b6d4;
}

.big-stat .label {
  font-size: 0.9rem;
  color: #94a3b8;
}

@media (max-width: 768px) {
  .cases-grid {
    grid-template-columns: 1fr;
  }
  
  .showcase-content {
    grid-template-columns: 1fr;
    text-align: center;
  }
  
  .showcase-image {
    font-size: 8rem;
  }
  
  .showcase-stats {
    grid-template-columns: 1fr;
  }
}
</style>
