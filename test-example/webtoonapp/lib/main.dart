import 'package:flutter/material.dart';
import 'package:webtoonapp/screens/home_screen.dart';
import 'package:webtoonapp/services/api_service.dart';

void main() {
  ApiSerice.getTodaysToons();
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: HomeScreen(),
    );
  }
}
