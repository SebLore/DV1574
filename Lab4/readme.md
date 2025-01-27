# Laboration 4

This is Laboration 4 for the course DV1574 Introduction to Programming with Python.

## Assignment instructions

Instructions provided in Swedish:

>### Generella krav
>
> Tänk på att koden ska vara väl strukturerad och uppdelad i flera olika funktioner (minst 5 st) på ett logiskt bra sätt.
>
> Inga globala variabler (förutom eventuella konstantvariabler) får användas inuti funktionerna. All information som funktionerna behöver få in eller leverera ut ska överföras via parametrar och returvärden.
>
> Programmet ska vara stabilt och ha nödvändig felhantering så att det inte kraschar, oavsett vad som händer under körning och oavsett vad användaren hittar på.
>
> Koden ska följa de riktlinjer vi ger i kursen angående läslighet och konventioner (PEP8).
    Dessa konventioner finns sammanställda i dokumentet 'Kodstil'.
>
>Tänk även på detta innan ni lämnar in:
>
> - Använd vettiga variabelnamn.
> - Använd konsekvent språk.
> - Skriv lagom mycket kommentarer.
> - Hårdkoda inte.
> - Var noga med att se till att ditt program uppfyller alla specifikationer i uppgiftsformuleringen.
>
> #### Uppgiftsspecifika krav
>
>Till det här inlämningstillfället finns det två olika uppgifter att välja emellan. Uppgifterna kommer från helt olika >tillämpningsområden, och ni väljer fritt vilken av uppgifterna ni vill arbeta med.
>
>Ni ska bara lämna in lösning på en av de två alternativa uppgifterna!
>
>Ni når uppgiftsbeskrivningarna för respektive uppgift via länkarna nedan.
>
>De allmänna anvisningarna på denna sida gäller oavsett vilken uppgift ni valt att arbeta med.

## Uppgiftsbeskrivning Laboration 4 - File Safe

### Förberedelser

Innan ni börjar med den här uppgiften ska följande introduktion gås igenom: "Introduktion till modulen os". Den är direkt förberedande för den här uppgiften.

Koden ni förväntas skriva förutsätter att också att ni använder någon valfri modul för kryptering t ex cryptography. Sådana externa moduler kräver att man först installerar dem. För att installera en modul skriver man i en terminal:

`pip install <modulnamnet>`

(Om du kör Linux eller MAC OS behöver du skriva pip3 istället för pip.)

Om du hellre vill implementera en egen modul (python-fil med funktioner som du kan anropa) för att få kryptering och dekryptering får du gärna göra det. Var i så fall noga med att dokumentera i din modul vilken krypteringasalgoritm du implementerat. Se också till att du lägger din Python-modul i samma mapp som du kör programmet ifrån så att interpretatorn kan hitta den.

### Uppgift File Safe

I den här uppgiften ska ni skriva ett program som skapar "säkerhetsskåp" för hemliga filer.

I programmet ska man kunna skapa mappar och text-filer, där filerna sparas i krypterad form, viket innebär att texten bara kan läsas från programmet. Om man tittar direkt i filen via filsystemet ska den inte vara möjlig att förstå.  

### Kravspecifikation

#### Meny-hantering

Programmet ska vara menybaserat och i huvudmenyn ska det finnas menyval för att:

    1. Skapa en ny mapp
    2. Välja en befintlig mapp
    0. Avsluta programmet

Om man väljer att skapa en ny mapp så ska användaren få välja namn för den nya mappen genom inmatning.
Om man väljer en befintlig mapp ska de mappar som finns att välja på presenteras, och ett val ska göras genom inmatning. Därefter ska användaren få välja mellan följande alternativ i en ny meny:

    1. Skapa en ny fil
    2. Läs en befintlig fil
    3. Lägg till text i en befintlig fil
    4. Ta bort en fil
    5. Gå tillbaka till huvudmenyn

Menyvalens nummer måste stämma med specifikationen!
Ditt program får ha fler meny-val om du vill.

Man ska kunna göra upprepade menyval under en programkörning.
*Programmet ska inte avslutas förrän menyvalet för att avsluta valts*.

### Implementationskrav

*Funktioner från en extern modul ska användas för kryptering och dekryptering.*

Alla kravställda funktioner som namnges nedan måste ligga i en fil som heter `file_safe.py`.
All er kod (förutom eventuella krypteringsfunktioner) kan ligga i den filen. Om ni valt att implementera egna funktioner för kryptering och dekryptering måste de ligga i en separat fil.

Följande funktioner ska finnas och måste anropas i koden. Dela upp koden i flera hjälpfunktioner där det passar.

`validate_choice(ok_list)`

Denna funktion ska ta in input från användaren och returnera det inmatade valet. Om inmatningen inte motsvarar något av värdena i listan som skickas in som argument, `ok_list`, ska ett felmeddelande skrivas ut och en ny inmatning krävas, detta ska fortsätta tills acceptabel input gjorts. Funktionen ska användas i ditt program för att validera inmatningar för meny-val ur menyer. Det betyder att inskickad `ok_list` ska innehålla alla acceptabla menyval i den aktuella menyn som valet ska valideras för.

Funktionen ska vara robust mot felaktiga inmatningar och begära en ny inmatning om användaren gjort en inmatning som inte duger, så att funktionen alltid returnerar ett giltigt val.

Huvudprogrammets kod ska ligga i en egen funktion som döps till main(). Denna funktion måste innehålla programmets huvud-loop (`while`-sats), den får inte vara rekursiv.

Ingen kod, förutom anropet till `main()` och eventuella konstantvariabler, får ligga globalt.

Kom ihåg att det är viktigt att det globala anropet till main() ligger inuti en speciell "magisk" `if`-sats (se nedan), som gör det möjligt att importera kod från kodfilen, annars kraschar test-programmet som testar funktionerna på EOFError.

    ```py
    if __name__ == "__main__":
        main()
    ```
Funktionsdefinitionerna ska inte stå inne i denna if-sats eftersom funktionerna då blir oåtkomliga och inte går att importera till andra program som t.ex testprogrammet..

## Implementation

Implementation details here
