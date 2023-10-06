using AsoSoftLibrary;

//recursive directory traversal
// find all files in the current directory and all subdirectories
//string[] files = Directory.GetFiles(@"..\test\batches\corpus", "*.*", SearchOption.AllDirectories);
string[] files = Directory.GetFiles(@"..\..\..\..\test\remaining corpus\remaining_corpus_crawler\corpus", "*.*", SearchOption.AllDirectories);

System.Console.WriteLine("Found {0} files", files.Length);

int i = 1;
foreach (string file in files)
{
    if (!file.Contains("link.txt") && !file.Contains("failed_links.txt"))
    {
        string text = File.ReadAllText(file);
        text = AsoSoft.Normalize(text, isOnlyKurdish: false, changeInitialR: true, deepUnicodeCorrectios: true, additionalUnicodeCorrections: true, new Dictionary<char, string>());
        text = AsoSoft.UnifyNumerals(text, "ar");
        text = AsoSoft.SeperateDigits(text);
        text = AsoSoft.NormalizePunctuations(text, false);
        text = AsoSoft.TrimLine(text);
        text = AsoSoft.ReplaceHtmlEntity(text);
        File.WriteAllText(file, text);
    }
    Console.Clear();
    System.Console.WriteLine("{0}/{1}", i++, files.Length);
}