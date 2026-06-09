<template>
  <div class="home">
    <section class="hero" @mousemove="handleMouseMove" @mouseleave="handleMouseLeave">
      <div class="binary-container">
        <span 
          v-for="(item, index) in binaryParticles" 
          :key="index"
          class="binary-text"
          :style="{
            left: item.x + 'px',
            top: item.y + 'px',
            opacity: item.opacity,
            fontSize: item.size + 'px',
            transform: `rotate(${item.rotation}deg)`
          }"
        >
          {{ item.value }}
        </span>
      </div>
      <div class="container">
        <div class="hero-content">
          <div class="hero-text">
            <h1>工业4.0智能解决方案</h1>
            <p>引领制造业数字化转型，打造智能工厂新时代</p>
            <div class="hero-buttons">
              <button class="btn btn-primary">了解更多</button>
              <button class="btn btn-secondary">查看案例</button>
            </div>
          </div>
          <div class="hero-visual">
            <div class="visual-box">
              <div class="hexagon"></div>
              <div class="hexagon"></div>
              <div class="hexagon"></div>
            </div>
          </div>
        </div>
        <div class="stats">
          <div class="stat-item">
            <span class="stat-number">500+</span>
            <span class="stat-label">服务企业</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">15+</span>
            <span class="stat-label">行业覆盖</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">98%</span>
            <span class="stat-label">客户满意度</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">10年</span>
            <span class="stat-label">行业经验</span>
          </div>
        </div>
      </div>
    </section>

    <section class="features">
      <div class="container">
        <div class="section-header">
          <h2>核心技术</h2>
          <p>基于工业4.0理念，提供全方位智能化解决方案</p>
        </div>
        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3>智能制造</h3>
            <p>自动化生产线、工业机器人集成、智能仓储系统</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">☁️</div>
            <h3>工业物联网</h3>
            <p>设备互联互通、实时数据采集、远程监控管理</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>数据分析</h3>
            <p>大数据分析、预测性维护、生产优化决策</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">🔧</div>
            <h3>设备集成</h3>
            <p>PLC编程、SCADA系统、MES制造执行系统</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">🔄</div>
            <h3>柔性生产</h3>
            <p>模块化设计、快速换线、定制化生产</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">🛡️</div>
            <h3>安全保障</h3>
            <p>工业网络安全、数据加密、权限管理</p>
          </div>
        </div>
      </div>
    </section>

    <section class="services">
      <div class="container">
        <div class="section-header">
          <h2>解决方案</h2>
          <p>针对不同行业，提供定制化的智能解决方案</p>
        </div>
        <div class="services-grid">
          <div class="service-card">
            <div class="service-image">🏭</div>
            <h3>汽车制造</h3>
            <p>自动化装配线、焊接机器人、质量检测系统</p>
            <button class="btn btn-outline">了解详情</button>
          </div>
          <div class="service-card">
            <div class="service-image">💊</div>
            <h3>医药行业</h3>
            <p>洁净车间自动化、药品追溯系统、智能仓储</p>
            <button class="btn btn-outline">了解详情</button>
          </div>
          <div class="service-card">
            <div class="service-image">📦</div>
            <h3>物流仓储</h3>
            <p>AGV搬运机器人、立体仓库、分拣系统</p>
            <button class="btn btn-outline">了解详情</button>
          </div>
        </div>
      </div>
    </section>

    <section class="news-preview">
      <div class="container">
        <div class="section-header">
          <h2>最新资讯</h2>
          <router-link to="/news" class="view-all">查看全部</router-link>
        </div>
        <div class="news-grid">
          <div class="news-card" v-for="news in latestNews" :key="news.id">
            <div class="news-date">{{ news.date }}</div>
            <h3>{{ news.title }}</h3>
            <p>{{ news.summary }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { reactive, onUnmounted } from 'vue'

const binaryParticles = reactive([])
let particleId = 0
let lastX = 0
let lastY = 0
let isMouseInside = false
let lastMoveTime = 0
let animationInterval = null

const updateParticles = () => {
  const now = Date.now()
  const mouseStopped = now - lastMoveTime > 500
  
  for (let i = binaryParticles.length - 1; i >= 0; i--) {
    const particle = binaryParticles[i]
    
    particle.x += particle.velocityX
    particle.y += particle.velocityY
    
    if (mouseStopped) {
      particle.opacity -= 0.08
    } else {
      particle.opacity -= 0.02
    }
    particle.size *= 0.98
    
    if (particle.opacity <= 0) {
      binaryParticles.splice(i, 1)
    }
  }
}

const handleMouseMove = (e) => {
  isMouseInside = true
  lastMoveTime = Date.now()
  
  const dx = e.clientX - lastX
  const dy = e.clientY - lastY
  const distance = Math.sqrt(dx * dx + dy * dy)
  
  if (distance > 10) {
    const rect = e.currentTarget.getBoundingClientRect()
    const x = e.clientX - rect.left
    const y = e.clientY - rect.top
    
    for (let i = 0; i < 3; i++) {
      const particle = {
        id: particleId++,
        x: x + (Math.random() - 0.5) * 30,
        y: y + (Math.random() - 0.5) * 30,
        value: Math.random() > 0.5 ? '0' : '1',
        size: 10 + Math.random() * 6,
        opacity: 0.9,
        rotation: (Math.random() - 0.5) * 20,
        velocityX: (Math.random() - 0.5) * 1.5,
        velocityY: (Math.random() - 0.5) * 1.5 - 0.5
      }
      binaryParticles.push(particle)
    }
    
    lastX = e.clientX
    lastY = e.clientY
  }
}

const handleMouseLeave = () => {
  isMouseInside = false
  binaryParticles.splice(0, binaryParticles.length)
}

animationInterval = setInterval(updateParticles, 30)

onUnmounted(() => {
  if (animationInterval) {
    clearInterval(animationInterval)
  }
})

const latestNews = reactive([
  {
    id: 1,
    date: '2026-06-01',
    title: '工业4.0技术助力制造业转型升级',
    summary: '新一代工业自动化技术正在深刻改变传统制造业的生产模式...'
  },
  {
    id: 2,
    date: '2026-05-28',
    title: '人工智能在智能制造中的应用',
    summary: 'AI技术与工业自动化的深度融合，开启智能工厂新纪元...'
  },
  {
    id: 3,
    date: '2026-05-20',
    title: '5G技术推动工业互联网发展',
    summary: '5G网络为工业设备互联互通提供了高速可靠的通信保障...'
  }
])
</script>

<style scoped>
.hero {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
  color: white;
  padding: 80px 0;
  position: relative;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 30% 50%, rgba(6, 182, 212, 0.1) 0%, transparent 50%);
}

.binary-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
}

.binary-text {
  position: absolute;
  font-family: 'Courier New', monospace;
  font-weight: bold;
  color: #06b6d4;
  text-shadow: 0 0 10px rgba(6, 182, 212, 0.8), 0 0 20px rgba(6, 182, 212, 0.5);
  transition: opacity 0.1s ease, transform 0.1s ease;
  z-index: 0;
}

.hero-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  align-items: center;
  position: relative;
  z-index: 1;
}

.hero-text h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, #06b6d4, #3b82f6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-text p {
  font-size: 1.2rem;
  color: #94a3b8;
  margin-bottom: 2rem;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
}

.btn {
  padding: 12px 30px;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background: linear-gradient(135deg, #06b6d4, #3b82f6);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(6, 182, 212, 0.3);
}

.btn-secondary {
  background: transparent;
  color: white;
  border: 2px solid #06b6d4;
}

.btn-secondary:hover {
  background: rgba(6, 182, 212, 0.1);
}

.btn-outline {
  background: transparent;
  color: #06b6d4;
  border: 1px solid #06b6d4;
  padding: 8px 20px;
  font-size: 0.9rem;
}

.btn-outline:hover {
  background: #06b6d4;
  color: white;
}

.hero-visual {
  display: flex;
  justify-content: center;
  align-items: center;
}

.visual-box {
  display: flex;
  gap: 20px;
}

.hexagon {
  width: 100px;
  height: 100px;
  background: linear-gradient(135deg, rgba(6, 182, 212, 0.2), rgba(59, 130, 246, 0.2));
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  animation: float 3s ease-in-out infinite;
}

.hexagon:nth-child(2) {
  animation-delay: 1s;
}

.hexagon:nth-child(3) {
  animation-delay: 2s;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

.stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  margin-top: 4rem;
  padding-top: 2rem;
  border-top: 1px solid #334155;
}

.stat-item {
  text-align: center;
}

.stat-number {
  display: block;
  font-size: 2.5rem;
  font-weight: bold;
  background: linear-gradient(135deg, #06b6d4, #3b82f6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-label {
  color: #94a3b8;
}

.features, .services, .news-preview {
  padding: 60px 0;
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
}

.section-header h2 {
  font-size: 2.2rem;
  margin-bottom: 0.5rem;
  color: #0f172a;
}

.section-header p {
  color: #64748b;
}

.section-header .view-all {
  float: right;
  color: #06b6d4;
  text-decoration: none;
  font-weight: 500;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  color: #0f172a;
  margin-bottom: 0.5rem;
}

.feature-card p {
  color: #64748b;
  font-size: 0.9rem;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.service-card {
  background: linear-gradient(135deg, #0f172a, #1e293b);
  padding: 2.5rem;
  border-radius: 12px;
  color: white;
  text-align: center;
  transition: transform 0.3s ease;
}

.service-card:hover {
  transform: translateY(-5px);
}

.service-image {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.service-card h3 {
  margin-bottom: 0.5rem;
}

.service-card p {
  color: #94a3b8;
  margin-bottom: 1.5rem;
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.news-card {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  transition: box-shadow 0.3s ease;
}

.news-card:hover {
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
}

.news-date {
  color: #06b6d4;
  font-size: 0.85rem;
  margin-bottom: 0.5rem;
}

.news-card h3 {
  color: #0f172a;
  margin-bottom: 0.5rem;
}

.news-card p {
  color: #64748b;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .hero-content {
    grid-template-columns: 1fr;
    text-align: center;
  }
  
  .hero-text h1 {
    font-size: 2rem;
  }
  
  .hero-buttons {
    justify-content: center;
  }
  
  .stats {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .section-header .view-all {
    float: none;
    display: block;
    margin-top: 1rem;
  }
}
</style>
