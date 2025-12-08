/**
 * Creating a sidebar enables you to:
 * - Create an ordered group of docs
 * - Render a sidebar in the docs site
 * - List of links in the sidebar
 *
 * It can be rendered by adding the sidebar name to the docs-plugin configuration.
 *
 * @type {import('@docusaurus/plugin-content-docs').SidebarsConfig}
 */
const sidebars = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Setup',
      items: [
        'setup/digital-twin-workstation',
        'setup/physical-ai-edge-kit',
        'setup/cloud-native',
      ],
    },
    {
      type: 'category',
      label: 'Module 1: ROS 2',
      items: [
        'module-1-ros2/M1-C1-ROS-2-Fundamentals',
        'module-1-ros2/M1-C2-Robot-Control-Pipeline',
        'module-1-ros2/M1-C3-URDF-SRDF-Robot-Description',
        'module-1-ros2/M1-C4-Packages-Launch-Architecture',
        'module-1-ros2/M1-C5-Sensor-Ecosystem',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: Digital Twin',
      items: [
        'module-2-digital-twin/M2-C1-Why-Digital-Twins-Matter',
        'module-2-digital-twin/M2-C2-Gazebo-Physics-Overview',
        'module-2-digital-twin/M2-C3-URDF-Gazebo-Pipeline',
        'module-2-digital-twin/M2-C4-Sensor-Simulation',
        'module-2-digital-twin/M2-C5-Unity-Visualization',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: NVIDIA Isaac',
      items: [
        'module-3-isaac/M3-C1-Isaac-Sim-Foundations',
        'module-3-isaac/M3-C2-Synthetic-Data-Sensors',
        'module-3-isaac/M3-C3-Isaac-ROS-Jetson-Pipeline',
        'module-3-isaac/M3-C4-Navigation-Path-Planning',
        'module-3-isaac/M3-C5-Sim-to-Real-Concepts',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: VLA & Humanoids',
      items: [
        'module-4-vla-humanoids/M4-C1-VLA-Foundations',
        'module-4-vla-humanoids/M4-C2-Voice-to-Action',
        'module-4-vla-humanoids/M4-C3-Cognitive-Task-Planning',
      ],
    },
  ],
};

module.exports = sidebars;