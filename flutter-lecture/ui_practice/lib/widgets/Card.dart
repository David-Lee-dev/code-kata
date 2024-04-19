import 'package:flutter/material.dart';

class MyCard extends StatelessWidget {
  final String text, shortText, balance;
  final IconData icon;
  final bool inverted;

  const MyCard({
    super.key,
    required this.text,
    required this.shortText,
    required this.balance,
    required this.icon,
    this.inverted = false,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      clipBehavior: Clip.hardEdge,
      decoration: BoxDecoration(
        color: inverted
            ? const Color.fromARGB(255, 226, 226, 226)
            : const Color.fromARGB(255, 52, 52, 52),
        borderRadius: BorderRadius.circular(20),
      ),
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  text,
                  style: TextStyle(
                    color: inverted ? Colors.black : Colors.white,
                    fontSize: 32,
                    fontWeight: FontWeight.w600,
                  ),
                ),
                const SizedBox(
                  height: 10,
                ),
                Row(
                  children: [
                    Text(
                      balance,
                      style: TextStyle(
                        color: inverted ? Colors.black : Colors.white,
                        fontSize: 20,
                      ),
                    ),
                    const SizedBox(
                      width: 5,
                    ),
                    Text(
                      shortText,
                      style: TextStyle(
                        color: inverted
                            ? Colors.black.withOpacity(0.8)
                            : Colors.white.withOpacity(0.8),
                        fontSize: 20,
                      ),
                    ),
                  ],
                ),
              ],
            ),
            Transform.scale(
              scale: 3,
              child: Transform.translate(
                offset: const Offset(-7, 6),
                child: Icon(
                  icon,
                  color: inverted ? Colors.black : Colors.white,
                  size: 50,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
