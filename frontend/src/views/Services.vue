<template>
  <div class="services">
    <section class="services-header">
      <div class="container">
        <h2>服务项目</h2>
        <p>我们提供全方位的企业服务解决方案</p>
      </div>
    </section>
    
    <section class="services-list">
      <div class="container">
        <div class="services-grid">
          <div class="service-card">
            <div class="icon">💼</div>
            <h3>企业咨询</h3>
            <p>提供专业的企业管理咨询服务，帮助企业制定发展战略，优化业务流程，提升运营效率。</p>
            <ul class="features">
              <li>战略规划</li>
              <li>流程优化</li>
              <li>绩效管理</li>
            </ul>
          </div>
          
          <div class="service-card">
            <div class="icon">💻</div>
            <h3>技术服务</h3>
            <p>提供一站式技术解决方案，包括软件开发、系统集成、云计算服务等，助力企业数字化转型。</p>
            <ul class="features">
              <li>软件开发</li>
              <li>系统集成</li>
              <li>云计算</li>
            </ul>
          </div>
          
          <div class="service-card">
            <div class="icon">📊</div>
            <h3>数据分析</h3>
            <p>利用先进的数据分析技术，帮助企业挖掘数据价值，做出精准决策，提升竞争力。</p>
            <ul class="features">
              <li>数据挖掘</li>
              <li>可视化分析</li>
              <li>预测分析</li>
            </ul>
          </div>
          
          <div class="service-card">
            <div class="icon">🎨</div>
            <h3>品牌设计</h3>
            <p>提供专业的品牌策划和设计服务，打造独特的品牌形象，提升品牌影响力。</p>
            <ul class="features">
              <li>品牌策划</li>
              <li>VI设计</li>
              <li>营销推广</li>
            </ul>
          </div>
          
          <div class="service-card">
            <div class="icon">🔒</div>
            <h3>安全服务</h3>
            <p>提供全面的网络安全解决方案，保护企业数据安全，防范网络威胁。</p>
            <ul class="features">
              <li>安全评估</li>
              <li>渗透测试</li>
              <li>安全运维</li>
            </ul>
          </div>
          
          <div class="service-card">
            <div class="icon">📱</div>
            <h3>移动应用</h3>
            <p>提供移动应用开发服务，包括iOS和Android平台，帮助企业拓展移动端业务。</p>
            <ul class="features">
              <li>iOS开发</li>
              <li>Android开发</li>
              <li>小程序开发</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>

<style scoped>
.services-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-align: center;
  padding: 60px 0;
}

.services-header h2 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.services-header p {
  font-size: 1.2rem;
}

.services-list {
  padding: 60px 0;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
}

.service-card {
  background-color: #f8f9fa;
  padding: 30px;
  border-radius: 10px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.service-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}

.icon {
  font-size: 3rem;
  margin-bottom: 15px;
}

.service-card h3 {
  font-size: 1.5rem;
  margin-bottom: 15px;
  color: #2c3e50;
}

.service-card p {
  color: #666;
  margin-bottom: 20px;
  line-height: 1.6;
}

.features {
  list-style: none;
}

.features li {
  padding: 8px 0;
  border-bottom: 1px solid #eee;
  color: #666;
}

.features li:last-child {
  border-bottom: none;
}
</style>
