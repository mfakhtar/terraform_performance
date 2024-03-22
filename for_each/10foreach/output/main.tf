resource "null_resource" "null" {
    for_each = {
        hArgOMZceS = "hArgOMZceS",
        QjBezteJtz = "QjBezteJtz",
        nyXwtqBoga = "nyXwtqBoga",
        jQtDLEEmsq = "jQtDLEEmsq",
        oIQclrXtdE = "oIQclrXtdE",
        RsAZYBBJQt = "RsAZYBBJQt",
        euNwuIFcRB = "euNwuIFcRB",
        dhCspvgwiZ = "dhCspvgwiZ",
        gOsLPVpCPZ = "gOsLPVpCPZ",
        FGltJtDrwZ = "FGltJtDrwZ"
    }
}

output "for_each_values" {
    value = { for key, value in null_resource.null : key => value.id }
}
