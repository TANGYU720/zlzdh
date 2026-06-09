<template>
  <div class="tutorials">
    <section class="page-header">
      <div class="container">
        <h1>技术教程</h1>
        <p>学习自动化技术，提升专业技能</p>
      </div>
    </section>

    <section class="tutorials-content">
      <div class="container">
        <div class="tutorial-sidebar">
          <div class="sidebar-section">
            <h3>技术分类</h3>
            <ul>
              <li :class="{ active: activeCategory === 'plc' }" @click="activeCategory = 'plc'">PLC编程</li>
              <li :class="{ active: activeCategory === 'scada' }" @click="activeCategory = 'scada'">SCADA系统</li>
              <li :class="{ active: activeCategory === 'robot' }" @click="activeCategory = 'robot'">工业机器人</li>
              <li :class="{ active: activeCategory === 'mes' }" @click="activeCategory = 'mes'">MES系统</li>
              <li :class="{ active: activeCategory === 'iot' }" @click="activeCategory = 'iot'">工业物联网</li>
            </ul>
          </div>
          <div class="sidebar-section">
            <h3>难度等级</h3>
            <ul>
              <li :class="{ active: activeLevel === 'all' }" @click="activeLevel = 'all'">全部难度</li>
              <li :class="{ active: activeLevel === 'beginner' }" @click="activeLevel = 'beginner'">入门</li>
              <li :class="{ active: activeLevel === 'intermediate' }" @click="activeLevel = 'intermediate'">中级</li>
              <li :class="{ active: activeLevel === 'advanced' }" @click="activeLevel = 'advanced'">高级</li>
            </ul>
          </div>
        </div>

        <div class="tutorial-main">
          <div class="tutorial-intro">
            <h2>自动化技术学习路径</h2>
            <p>从基础到进阶，系统学习工业自动化技术。我们提供PLC编程、SCADA系统、工业机器人等专业教程。</p>
          </div>

          <div class="tutorial-list">
            <div class="tutorial-card" v-for="tutorial in filteredTutorials" :key="tutorial.id">
              <div class="tutorial-icon">{{ tutorial.icon }}</div>
              <div class="tutorial-info">
                <div class="tutorial-meta">
                  <span class="level" :class="tutorial.level">{{ getLevelName(tutorial.level) }}</span>
                  <span class="category">{{ tutorial.category }}</span>
                </div>
                <h3>{{ tutorial.title }}</h3>
                <p>{{ tutorial.summary }}</p>
                <div class="tutorial-details">
                  <span>⏱️ {{ tutorial.duration }}</span>
                  <span>📚 {{ tutorial.lessons }} 节课</span>
                  <span>👥 {{ tutorial.students }} 人学习</span>
                </div>
                <button class="start-learning">开始学习 →</button>
              </div>
            </div>
          </div>

          <div class="learning-paths">
            <h2>学习路径推荐</h2>
            <div class="paths-grid">
              <div class="path-card">
                <div class="path-icon">🔧</div>
                <h3>PLC工程师成长之路</h3>
                <p>从零基础到PLC编程高手的完整学习路径</p>
                <div class="path-steps">
                  <span>Step 1: 电气基础</span>
                  <span>Step 2: PLC原理</span>
                  <span>Step 3: 编程实践</span>
                  <span>Step 4: 项目实战</span>
                </div>
                <button class="view-path">查看路径</button>
              </div>
              <div class="path-card">
                <div class="path-icon">🤖</div>
                <h3>工业机器人应用工程师</h3>
                <p>掌握工业机器人编程与调试技能</p>
                <div class="path-steps">
                  <span>Step 1: 机器人基础</span>
                  <span>Step 2: 示教编程</span>
                  <span>Step 3: 离线编程</span>
                  <span>Step 4: 集成调试</span>
                </div>
                <button class="view-path">查看路径</button>
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

const activeCategory = ref('plc')
const activeLevel = ref('all')

const tutorials = ref([
  {
    id: 1,
    title: 'PLC入门教程：从零基础到独立编程',
    summary: '系统学习PLC基础知识，掌握梯形图、功能块等编程方法，学会独立完成小型自动化项目。',
    icon: '🔌',
    category: 'PLC编程',
    level: 'beginner',
    duration: '20小时',
    lessons: 15,
    students: 2580
  },
  {
    id: 2,
    title: '西门子S7-1200 PLC高级编程',
    summary: '深入学习西门子S7-1200系列PLC，掌握结构化编程、数据块管理、通信等高级技能。',
    icon: '🔧',
    category: 'PLC编程',
    level: 'intermediate',
    duration: '30小时',
    lessons: 20,
    students: 1850
  },
  {
    id: 3,
    title: 'SCADA系统设计与开发',
    summary: '学习SCADA系统原理，掌握WinCC、Intouch等主流软件的使用，学会设计监控系统。',
    icon: '📊',
    category: 'SCADA系统',
    level: 'intermediate',
    duration: '25小时',
    lessons: 18,
    students: 1200
  },
  {
    id: 4,
    title: '工业机器人示教编程实战',
    summary: '掌握工业机器人基本操作，学会示教编程、轨迹规划、I/O控制等实用技能。',
    icon: '🤖',
    category: '工业机器人',
    level: 'beginner',
    duration: '15小时',
    lessons: 12,
    students: 980
  },
  {
    id: 5,
    title: 'MES系统原理与实施',
    summary: '了解MES制造执行系统架构，掌握系统选型、实施方法和运维技巧。',
    icon: '🏭',
    category: 'MES系统',
    level: 'advanced',
    duration: '35小时',
    lessons: 22,
    students: 650
  },
  {
    id: 6,
    title: '工业物联网网关开发',
    summary: '学习工业物联网技术，掌握MQTT、OPC UA等通信协议，开发物联网网关应用。',
    icon: '🌐',
    category: '工业物联网',
    level: 'advanced',
    duration: '40小时',
    lessons: 25,
    students: 480
  },
  {
    id: 7,
    title: '欧姆龙PLC编程入门',
    summary: '学习欧姆龙CP系列PLC编程，掌握指令系统和实际应用案例。',
    icon: '🔌',
    category: 'PLC编程',
    level: 'beginner',
    duration: '18小时',
    lessons: 14,
    students: 1350
  },
  {
    id: 8,
    title: '工业机器人离线编程',
    summary: '学习RobotStudio等离线编程软件，掌握离线编程、仿真和优化技巧。',
    icon: '💻',
    category: '工业机器人',
    level: 'intermediate',
    duration: '28小时',
    lessons: 20,
    students: 720
  }
])

const filteredTutorials = computed(() => {
  let result = tutorials.value
  if (activeLevel.value !== 'all') {
    result = result.filter(t => t.level === activeLevel.value)
  }
  return result
})

const getLevelName = (level) => {
  const names = {
    beginner: '入门',
    intermediate: '中级',
    advanced: '高级'
  }
  return names[level] || '未知'
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

.tutorials-content {
  padding: 40px 0;
}

.tutorials-content .container {
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 2rem;
}

.tutorial-sidebar {
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

.tutorial-main {
  background: white;
  border-radius: 8px;
  padding: 2rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.tutorial-intro {
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e2e8f0;
}

.tutorial-intro h2 {
  color: #0f172a;
  margin-bottom: 0.5rem;
}

.tutorial-intro p {
  color: #64748b;
}

.tutorial-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.tutorial-card {
  display: flex;
  gap: 1.5rem;
  padding: 1.5rem;
  background: #f8fafc;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.tutorial-card:hover {
  background: #f1f5f9;
  transform: translateX(5px);
}

.tutorial-icon {
  font-size: 3rem;
  flex-shrink: 0;
}

.tutorial-info {
  flex: 1;
}

.tutorial-meta {
  display: flex;
  gap: 1rem;
  margin-bottom: 0.5rem;
}

.level {
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 500;
}

.level.beginner {
  background: #dcfce7;
  color: #16a34a;
}

.level.intermediate {
  background: #fef3c7;
  color: #d97706;
}

.level.advanced {
  background: #fecaca;
  color: #dc2626;
}

.category {
  color: #06b6d4;
  font-size: 0.9rem;
}

.tutorial-info h3 {
  color: #0f172a;
  margin-bottom: 0.5rem;
}

.tutorial-info p {
  color: #64748b;
  margin-bottom: 1rem;
}

.tutorial-details {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1rem;
  color: #94a3b8;
  font-size: 0.9rem;
}

.start-learning {
  background: linear-gradient(135deg, #06b6d4, #3b82f6);
  color: white;
  border: none;
  padding: 0.6rem 1.5rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.3s;
}

.start-learning:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(6, 182, 212, 0.3);
}

.learning-paths {
  margin-top: 3rem;
  padding-top: 2rem;
  border-top: 1px solid #e2e8f0;
}

.learning-paths h2 {
  color: #0f172a;
  margin-bottom: 1.5rem;
}

.paths-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.5rem;
}

.path-card {
  background: linear-gradient(135deg, #0f172a, #1e293b);
  padding: 2rem;
  border-radius: 12px;
  color: white;
}

.path-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.path-card h3 {
  margin-bottom: 0.5rem;
}

.path-card p {
  color: #94a3b8;
  margin-bottom: 1rem;
}

.path-steps {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.path-steps span {
  color: #cbd5e1;
  font-size: 0.9rem;
  padding-left: 1rem;
  position: relative;
}

.path-steps span::before {
  content: '→';
  position: absolute;
  left: 0;
  color: #06b6d4;
}

.view-path {
  background: transparent;
  border: 1px solid #06b6d4;
  color: #06b6d4;
  padding: 0.6rem 1.5rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s;
}

.view-path:hover {
  background: #06b6d4;
  color: white;
}

@media (max-width: 768px) {
  .tutorials-content .container {
    grid-template-columns: 1fr;
  }
  
  .tutorial-card {
    flex-direction: column;
  }
  
  .paths-grid {
    grid-template-columns: 1fr;
  }
}
</style>
