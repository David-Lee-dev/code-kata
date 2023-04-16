import 'package:flutter/material.dart';
import 'package:pomodoro/screens/home_screen.dart';

void main() {
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        textTheme: const TextTheme(
          displayLarge: TextStyle(
            color: Color(0xFF232B55),
          ),
        ),
        cardColor: const Color(0xFFF4EDDB),
        colorScheme: const ColorScheme(
          background: Color(0xFFE7626C),
          brightness: Brightness.light,
          error: Color(0xFFE7626C),
          onBackground: Color(0xFF232B55),
          onError: Color(0xFFF4EDDB),
          onPrimary: Color(0xFFF4EDDB),
          onSecondary: Color(0xFFF4EDDB),
          onSurface: Color(0xFF232B55),
          primary: Color(0xFFE7626C),
          secondary: Color(0xFFE7626C),
          surface: Color(0xFFF4EDDB),
        ),
      ),
      home: const HomeScreen(),
    );
  }
}
