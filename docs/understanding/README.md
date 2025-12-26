# Dokumentasi Pemahaman Timetable-SA

Selamat datang di dokumentasi komprehensif untuk memahami logika core algoritma dari package Timetable-SA. Dokumentasi ini dirancang untuk memberikan pemahaman mendalam tentang bagaimana package ini bekerja, dari konsep dasar hingga implementasi lengkap.

## 📚 Daftar Isi

### 1. [Konsep Dasar dan Arsitektur](./01-konsep-dasar.md)
- Pengenalan Simulated Annealing
- Arsitektur package Timetable-SA
- Komponen-komponen utama
- Flow algoritma tingkat tinggi

### 2. [Arsitektur dan Algoritma Detail](./02-arsitektur-dan-algoritma.md)
- Detail implementasi Simulated Annealing
- Dua fase optimasi (Hard & Soft Constraints)
- Adaptive operator selection
- Reheating mechanism
- Fitness calculation
- Performance considerations

### 3. [API Reference Lengkap](./03-api-reference.md)
- SimulatedAnnealing class
- Constraint interface
- MoveGenerator interface
- SAConfig interface
- Type definitions
- Usage examples
- Error handling

### 4. [Implementasi dan Contoh Lengkap](./04-implementasi-dan-contoh.md)
- Studi kasus: University Course Timetabling
- Struktur proyek examples/timetabling
- Domain types definition
- Data loading implementation
- Initial solution generation
- Constraints implementation
- Move generators implementation
- Advanced features
- Best practices

### 5. [Visualisasi dan Diagram Alur](./05-visualisasi-dan-diagram.md)
- High-level architecture diagrams
- Algorithm flow charts
- Constraint system visualization
- Move generator selection
- Data flow diagrams
- Performance analysis
- Error handling flows

## 🎯 Target Audience

Dokumentasi ini ditujukan untuk:

1. **Developers** yang ingin mengintegrasikan Timetable-SA ke dalam proyek mereka
2. **Researchers** yang mempelajari algoritma optimasi dan constraint satisfaction
3. **Students** yang belajar tentang metaheuristic algorithms
4. **System Architects** yang merancang sistem penjadwalan
5. **Technical Managers** yang perlu memahami kapabilitas package

## 🚀 Quick Start

### Prerequisites
- Node.js >= 18.0.0
- TypeScript knowledge
- Basic understanding of optimization algorithms

### Installation
```bash
npm install timetable-sa
```

### Basic Usage
```typescript
import { SimulatedAnnealing } from 'timetable-sa';

// Define your problem-specific components
const constraints = [/* your constraints */];
const moveGenerators = [/* your move generators */];
const config = {
  initialTemperature: 1000,
  minTemperature: 0.01,
  coolingRate: 0.995,
  maxIterations: 50000,
  hardConstraintWeight: 10000,
  cloneState: (state) => JSON.parse(JSON.stringify(state)),
};

// Create and run solver
const solver = new SimulatedAnnealing(
  initialState,
  constraints,
  moveGenerators,
  config
);

const solution = solver.solve();
console.log('Best fitness:', solution.fitness);
```

## 🏗️ Core Concepts

### Simulated Annealing
Timetable-SA menggunakan algoritma **Simulated Annealing** dengan implementasi khusus:
- **Two-phase optimization**: Fokus hard constraints dulu, baru soft constraints
- **Adaptive operator selection**: Memilih move generator berdasarkan success rate
- **Reheating mechanism**: Escape dari local minima
- **Temperature-dependent moves**: Menyesuaikan intensitas move dengan temperature

### Constraint System
- **Hard Constraints**: WAJIB dipenuhi (penalty sangat tinggi)
- **Soft Constraints**: Preferensi (penalty ringan dengan weight)
- **Flexible Scoring**: Binary (0/1) untuk hard, gradual (0-1) untuk soft
- **Detailed Violation Reporting**: Deskripsi human-readable untuk setiap violation

### Move Generators
- **Targeted Operators**: Fokus pada perbaikan violation spesifik
- **General Operators**: Untuk eksplorasi dan optimasi
- **Constraint-Aware**: Generate valid moves ketika memungkinkan
- **Temperature-Dependent**: Adjust move intensity berdasarkan temperature

## 📊 Performance Characteristics

### Computational Complexity
- **Time**: O(iterations × constraints × moves)
- **Space**: O(state size + constraint data)

### Typical Performance
- **Small problems** (< 100 classes): < 1 minute
- **Medium problems** (100-500 classes): 5-15 minutes
- **Large problems** (500+ classes): 30+ minutes

### Optimization Factors
- Problem complexity
- Number of constraints
- Quality of initial solution
- Parameter tuning
- Hardware specifications

## 🔧 Advanced Features

### Custom Domain Types
Package ini dirancang untuk **generic** dan **unopinionated**:
- Custom state definitions
- Domain-specific constraints
- Specialized move operators
- Custom evaluation functions

### Hybrid Approaches
- Combine with other algorithms
- Multi-objective optimization
- Dynamic constraint adjustment
- Parallel evaluation

### Integration Patterns
- REST API integration
- Database persistence
- Real-time updates
- Web interface

## 🛠️ Development Workflow

### 1. Problem Analysis
- Identify constraints
- Define domain types
- Design state representation

### 2. Implementation
- Create constraint classes
- Implement move generators
- Configure algorithm parameters

### 3. Testing
- Unit test constraints
- Integration test moves
- Performance testing

### 4. Optimization
- Parameter tuning
- Performance profiling
- Result validation

### 5. Deployment
- Integration testing
- User acceptance testing
- Production deployment

## 📈 Best Practices

### Constraint Design
1. **Hard Constraints**: Binary scoring, fundamental requirements
2. **Soft Constraints**: Gradual scoring, weighted by importance
3. **Efficient Evaluation**: Use caching for expensive computations
4. **Clear Messages**: Provide actionable violation descriptions

### Move Generator Design
1. **Temperature Awareness**: Adjust move intensity based on temperature
2. **Constraint Awareness**: Generate valid moves when possible
3. **Targeted Operators**: Create specific operators for common violations
4. **Success Tracking**: Monitor operator effectiveness

### Parameter Tuning
1. **Start Conservative**: Begin with moderate parameters
2. **Monitor Progress**: Use logging to track optimization
3. **Adjust Based on Results**: Tune parameters based on solution quality
4. **Consider Problem Size**: Scale parameters with problem complexity

## 🐛 Common Issues and Solutions

### No Convergence
- Increase initial temperature
- Decrease cooling rate
- Add more targeted operators
- Improve initial solution

### Too Many Violations
- Increase hard constraint weight
- Add specific move operators
- Check constraint implementation
- Verify data quality

### Slow Performance
- Optimize state cloning
- Use constraint caching
- Reduce problem complexity
- Parallelize evaluation

### Local Optima
- Enable reheating mechanism
- Increase exploration moves
- Add operator diversity
- Use higher initial temperature

## 🔍 Debugging and Monitoring

### Logging Configuration
```typescript
const config = {
  logging: {
    enabled: true,
    level: 'debug',
    logInterval: 500,
    output: 'both',
    filePath: './optimization.log',
  },
};
```

### Performance Monitoring
- Track convergence rate
- Monitor operator statistics
- Analyze violation patterns
- Measure execution time

### Result Validation
- Check all hard constraints satisfied
- Verify all classes scheduled
- Validate room assignments
- Confirm lecturer availability

## 🚀 Extension Ideas

### Multi-Objective Optimization
- Balance multiple competing objectives
- Pareto frontier analysis
- Weighted sum approaches

### Dynamic Constraints
- Time-varying constraints
- User preference integration
- Real-time constraint updates

### Hybrid Algorithms
- Combine with genetic algorithms
- Local search refinement
- Machine learning integration

### Advanced Features
- Distributed optimization
- Cloud-based scaling
- Real-time collaboration
- Mobile interfaces

## 📞 Support and Contributing

### Getting Help
- Check this documentation
- Review examples in `/examples`
- Examine test cases in `/tests`
- Check GitHub issues

### Contributing
- Fork the repository
- Create feature branch
- Add tests for new features
- Submit pull request

### Community
- GitHub discussions
- Stack Overflow questions
- Blog posts and tutorials
- Conference presentations

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.

## 🙏 Acknowledgments

- Simulated Annealing algorithm pioneers
- Constraint satisfaction research community
- Open source contributors
- University partners for real-world testing

---

**Catatan**: Dokumentasi ini terus diperbarui sesuai dengan perkembangan package. Untuk informasi terbaru, selalu periksa versi terbaru dari package Timetable-SA.

## 📚 Additional Resources

### Academic Papers
- "Simulated Annealing: Theory and Applications" - Kirkpatrick et al.
- "Constraint Satisfaction Problems" - Tsang
- "Metaheuristic Optimization" - Luke

### Online Resources
- [Simulated Annealing Tutorial](https://en.wikipedia.org/wiki/Simulated_annealing)
- [Constraint Programming](https://en.wikipedia.org/wiki/Constraint_programming)
- [Optimization Algorithms](https://en.wikipedia.org/wiki/Mathematical_optimization)

### Related Projects
- [OR-Tools](https://developers.google.com/optimization)
- [Choco Solver](https://choco-solver.org/)
- [JsOptimization](https://github.com/josdejong/mathjs)

---

**Happy Optimizing!** 🎉