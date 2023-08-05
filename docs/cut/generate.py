
for i in range(40):
    j = str(1001 + i)[-3:]
    file_name = f"T{j}"
    # print(file_name, end="\t")
    f = open(f"{file_name}.html", "w", encoding="utf-8")
    f.write(f'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- include handeler -->
    <script src="https://unpkg.com/htmlincludejs"></script>
    <!-- ------------------------- -->

    <!-- load google fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap" rel="stylesheet">
    <!-- ------------------------- -->

    <!-- load css files -->
    <link rel="stylesheet" href="../style/style.css" type="text/css">
    <link rel="stylesheet" href="../style/tailwind.css" type="text/css">
    <!-- ------------------------- -->

    <title>cut {file_name}</title>
</head>

<body>

    <include src="../navbar.html"></include>


    <div class="flex items-center p-4 mb-4 mt-4  text-sm text-red-800 border border-red-300 rounded-lg bg-red-100 dark:bg-gray-800 dark:text-red-400 dark:border-red-800"
        role="alert">
        <svg class="flex-shrink-0 inline w-4 h-4 mr-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
            fill="currentColor" viewBox="0 0 20 20">
            <path
                d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
        </svg>
        <span class="sr-only">Info</span>
        <div class="font-vazir">
            متاسفانه اطلاعات برش مورد نظر هنوز در سامانه ثبت نشده‌است.
        </div>
    </div>

    <div class="font-vazir text-right relative overflow-x-auto shadow-md rounded-lg mt-4">
        <table class="text-right w-full text-sm text-left ">

            <tbody>
                <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 ">
                    <th class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">
                        نام تولیدی:
                    </th>
                    <td class="border-l px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">

                    </td>

                    <th class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">
                        تعداد طاقه‌ها:
                    </th>
                    <td class="px-6 py-4 border-l hover:bg-gray-50 dark:hover:bg-gray-600">

                    </td>

                    <th class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">
                        مصرف هر کار:
                    </th>
                    <td class="px-6 py-4 border-l hover:bg-gray-50 dark:hover:bg-gray-600">

                    </td>

                    <th class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">
                        کد:
                    </th>
                    <td class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">

                    </td>
                </tr>

                <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 ">
                    <th class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">
                        سایزبندی:
                    </th>
                    <td class="px-6 py-4 border-l hover:bg-gray-50 dark:hover:bg-gray-600">

                    </td>

                    <th class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">
                        تعداد طاقه‌ خرج‌کار:
                    </th>
                    <td class="px-6 py-4 border-l hover:bg-gray-50 dark:hover:bg-gray-600">

                    </td>

                    <th class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">
                        مصرف لایی هر کار:
                    </th>
                    <td class="px-6 py-4 border-l hover:bg-gray-50 dark:hover:bg-gray-600">

                    </td>

                    <th class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">
                        تاریخ:
                    </th>
                    <td class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">

                    </td>
                </tr>
                <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 ">
                    <th class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">
                        نام مدل:
                    </th>
                    <td class="px-6 py-4 border-l hover:bg-gray-50 dark:hover:bg-gray-600">

                    </td>

                    <th class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">
                        نوع پارچه:
                    </th>
                    <td class="px-6 py-4 border-l hover:bg-gray-50 dark:hover:bg-gray-600">

                    </td>

                    <th class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">
                        طول خط‌کشی
                    </th>
                    <td class="px-6 py-4 border-l hover:bg-gray-50 dark:hover:bg-gray-600">

                    </td>

                    <th class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">
                        کد مدل
                    </th>
                    <td class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-600">

                    </td>
                </tr>
            </tbody>
        </table>
    </div>


    <div class="font-vazir text-right relative overflow-x-auto shadow-md rounded-lg mt-4">
        <table class="text-right w-full text-sm text-left text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 uppercase border-b bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" class="w-[35px] border-l">
                    </th>
                    <th scope="col" class="px-6 py-3">
                        رنگ
                    </th>
                    <th scope="col" class="px-6 py-3 w-32">
                        متراژ
                    </th>
                    <th scope="col" class="px-6 py-3 w-32">
                        عرض
                    </th>
                    <th scope="col" class="px-6 py-3 w-32">
                        تعداد لا
                    </th>
                    <th scope="col" class="px-6 py-3 w-32">
                        تعداد کار
                    </th>
                    <th scope="col" class="px-6 py-3 w-32">
                        تعداد لا خرج‌کار
                    </th>
                    <th scope="col" class="px-6 py-3 w-96">
                        توضیحات
                    </th>
                </tr>
            </thead>

            <tbody>
                <!-- #1 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #2 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #3 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #4 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #5 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #6 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #7 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #8 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #9 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #10 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #11 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #12 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #13 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #14 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>
                <!-- #15 -->
                <tr
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">

                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                </tr>


                <tr
                    class=" border-b text-black text-bold bg-gray-100 dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <td scope="row" class="text-center pr-[20px] pl-2 border-l">

                    </td>
                    <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                        کل
                    </th>
                    <td class="px-6 py-4 ">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">
                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">

                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">
                    </td>
                    <td class="px-6 py-4 font-vazir-fadigit">
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

</body>
<script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.4/flowbite.min.js"></script>

</html>''')
    f.close()
